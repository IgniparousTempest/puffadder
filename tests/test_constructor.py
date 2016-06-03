import unittest

from constructor import constructor


@constructor
class Foo(object):
    def __init__(self, name="Lisa", age=12):
        pass

    def bar(self):
        return "bar"


@constructor
class Bar(object):
    """Class is pointless"""
    def __init__(self, name="Lisa", age=12):
        self._hidden_var = 1


@constructor
class Baz(object):
    def __init__(self, new, name="Lisa", age=12):
        """The doc"""
        self.new = new
        self.name = "Steve"
        self._hidden_var = 1


@constructor
class FooBar(object):
    def __init__(self, name, age=12):
        self.name = name + " Pitcher"
        self._hidden_var = 1


class BuildtargetTests(unittest.TestCase):
    def test_constructor_ignores_functions(self):
        foo = Foo(
            name="Matthew",
            age=22
        )
        self.assertEqual(foo.name, "Matthew")
        self.assertEqual(foo.age, 22)
        self.assertEqual(foo.bar(), "bar")

    def test_constructor_raises_type_error_if_argument_is_missing(self):
        expected_error_message = "__init__() missing 1 required positional argument: 'age'"

        with self.assertRaises(TypeError) as cm:
            bar = Bar(
                name="Trevor"
            )

        self.assertEqual(str(cm.exception), expected_error_message)

    def test_constructor_raises_type_error_if_too_many_arguments_present_and_constructor(self):
        expected_error_message = "__init__() missing 1 required positional argument: 'new'"

        with self.assertRaises(TypeError) as cm:
            baz = Baz(
                name="Jonah",
                age=22,
                other="Jewish"
            )

        self.assertEqual(str(cm.exception), expected_error_message)

    def test_constructor_raises_type_error_if_too_many_arguments_present_and_no_constructor(self):
        expected_error_message = "__init__() got an unexpected keyword argument 'other'"

        with self.assertRaises(TypeError) as cm:
            bar = Bar(
                name="David",
                age=23,
                other="Mohamed"
            )

        self.assertEqual(str(cm.exception), expected_error_message)

    def test_constructor_ignores_private_attributes(self):
        bar = Bar(
            name="Peter",
            age=25
        )
        self.assertEqual(bar.name, "Peter")
        self.assertEqual(bar.age, 25)

    def test_constructor_preserves_original_init(self):
        baz = Baz(
            name="Courtney",
            age=24,
            new=False
        )
        self.assertEqual(baz.name, "Steve")
        self.assertEqual(baz.age, 24)
        self.assertEqual(baz.new, False)

    def test_constructor_preserves_original_init_with_duplicate_init_parameters(self):
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
