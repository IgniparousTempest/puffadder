import unittest

from builder import builder


@builder
class Foo(object):
    def bar(self):
        pass

    name = "Lisa"
    age = 12


@builder
class Bar(object):
    """Class is pointless"""
    _hidden_var = 1
    name = "Lisa"
    age = 12


@builder
class Baz(object):
    def __init__(self, new):
        """The doc"""
        self.new = new
        self.name = "Steve"
    _hidden_var = 1
    name = "Lisa"
    age = 12


@builder
class FooBar(object):
    def __init__(self, name):
        self.name = name + " Pitcher"
    _hidden_var = 1
    name = "Lisa"
    age = 12


class BuildtargetTests(unittest.TestCase):
    def test_to_string_ignores_functions(self):
        foo = Foo(
            name="Matthew",
            age=22
        )
        self.assertEqual(foo.name, "Matthew")
        self.assertEqual(foo.age, 22)

    def test_to_string_raises_type_error_if_argument_is_missing(self):
        expected_error_message = "__init__() missing 1 required positional argument: 'age'"

        with self.assertRaises(TypeError) as cm:
            bar = Bar(
                name="Trevor"
            )

        self.assertEqual(str(cm.exception), expected_error_message)

    def test_to_string_raises_type_error_if_too_many_arguments_present_and_constructor(self):
        expected_error_message = "__init__() got an unexpected keyword argument 'other'"

        with self.assertRaises(TypeError) as cm:
            baz = Baz(
                name="Jonah",
                age=22,
                other="Jewish"
            )

        self.assertEqual(str(cm.exception), expected_error_message)

    def test_to_string_raises_type_error_if_too_many_arguments_present_and_no_constructor(self):
        expected_error_message = "__init__() got an unexpected keyword argument 'other'"

        with self.assertRaises(TypeError) as cm:
            bar = Bar(
                name="David",
                age=23,
                other="Mohamed"
            )

        self.assertEqual(str(cm.exception), expected_error_message)

    def test_to_string_ignores_private_attributes(self):
        bar = Bar(
            name="Peter",
            age=25
        )
        self.assertEqual(bar.name, "Peter")
        self.assertEqual(bar.age, 25)

    def test_to_string_preserves_original_init(self):
        baz = Baz(
            name="Courtney",
            age=24,
            new=False
        )
        self.assertEqual(baz.name, "Steve")
        self.assertEqual(baz.age, 24)
        self.assertEqual(baz.new, False)

    def test_to_string_preserves_original_init_with_duplicate_init_parameters(self):
        foobar = FooBar(
            name="Courtney",
            age=24
        )
        self.assertEqual(foobar.name, "Courtney Pitcher")
        self.assertEqual(foobar.age, 24)

    def test_buildtarget_does_not_override_class_doc(self):
        self.assertEqual(Bar.__doc__, "Class is pointless")
        self.assertEqual(Foo.__doc__, None)

    def test_buildtarget_does_not_override_init_method_doc(self):
        self.assertEqual(Baz.__init__.__doc__, "The doc")
        self.assertEqual(FooBar.__init__.__doc__, None)


if __name__ == '__main__':
    unittest.main()
