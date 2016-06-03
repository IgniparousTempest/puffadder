def constructor(original_class):
    """
    Adds a __init__ function with all class attributes as parameters.
    If there is an __init__ defined already, it applies the generated one and then the original one.

    e.g.:
    @constructor
    class Foo(object):
        def __init__(self, name, age=22):
            self._internal_attribute = "This will not be set"

        def bar(self):
            pass

    foo = Foo(
        name="Johan",
        age=32
    )
    """

    original_init = original_class.__init__

    # Gets all public class attributes
    attributes = []
    # Get parameters in original init
    if hasattr(original_init, "__code__"):
        attributes = original_init.__code__.co_varnames[1:]

    def __init__(self, **kwargs):
        for attr in attributes:
            try:
                self.__dict__[attr] = kwargs[attr]
            except KeyError:
                raise TypeError("__init__() missing 1 required positional argument: '{}'".format(attr))

        if hasattr(original_init, "__code__"):
            original_init(self, **kwargs)
        else:
            original_init(self)
    __init__.__doc__ = original_init.__doc__

    original_class.__init__ = __init__
    return original_class
