import unittest

from to_string import to_string


@to_string
class Foo(object):
    def bar(self):
        pass

    name = "Lisa"
    age = 12


@to_string
class Bar(object):
    """Class is pointless"""
    _hidden_var = 1
    name = "Lisa"
    age = 12


@to_string
class Baz(object):
    def __init__(self, new):
        self.new = new
    _hidden_var = 1
    name = "Lisa"
    age = 12


class BuildtargetTests(unittest.TestCase):
    def test_to_string_ignores_functions(self):
        foo = Foo()
        self.assertEqual(str(foo), "{age=12, name=Lisa}")

    def test_to_string_ignores_private_attributes(self):
        bar = Bar()
        self.assertEqual(str(bar), "{age=12, name=Lisa}")

    def test_to_string_returns_instance_attributes(self):
        bar = Bar()
        bar.age = 22
        bar.name = "Jonah"
        self.assertEqual(str(bar), "{age=22, name=Jonah}")

    def test_to_string_attributes_defined_with_self_are_not_returned(self):
        baz = Baz(True)
        self.assertEqual(str(baz), "{age=12, name=Lisa}")

    def test_buildtarget_does_not_override_method_doc(self):
        self.assertEqual(Bar.__doc__, "Class is pointless")
        self.assertEqual(Foo.__doc__, None)


if __name__ == '__main__':
    unittest.main()
