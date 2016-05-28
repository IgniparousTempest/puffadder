# Possibly consider using exec, so that we can see the names. Could be dangerous though, so I'm not sure.
def builder(original_class):
    """
    Adds a __init__ function with all class attributes as parameters.
    If there is an __init__ defined already, it applies the generated one and then the original one.

    e.g.:
    @builder
    class Foo(object):
        _internal_attribute = "This will not be set"
        name = "Lisa"
        age = 12

        def bar(self):
            pass

    foo = Foo(
        name="Johan",
        age=32
    )
    """

    # Gets all public class attributes
    attributes = [attr for attr in dir(original_class) if
                  not attr.startswith("_") and
                  attr in original_class.__dict__ and
                  not hasattr(original_class.__dict__[attr], "__call__")]

    original_init = original_class.__init__

    def __init__(self, **kwargs):
        # Get parameters in original init
        original_parameters = []
        if hasattr(original_init, "__code__"):
            original_parameters = original_init.__code__.co_varnames[1:]

        for attr in attributes:
            try:
                self.__dict__[attr] = kwargs[attr]
                # preserve input for original init
                if attr not in original_parameters:
                    del kwargs[attr]
            except KeyError:
                raise TypeError("__init__() missing 1 required positional argument: '{}'".format(attr))

        if hasattr(original_init, "__code__"):
            original_init(self, **kwargs)
        else:
            if len(kwargs) > 0:
                raise TypeError("__init__() got an unexpected keyword argument '{}'".format(next(iter(kwargs.keys()))))
            original_init(self)
    __init__.__doc__ = original_init.__doc__

    original_class.__init__ = __init__
    return original_class
