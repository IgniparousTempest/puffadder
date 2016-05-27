# Possibly consider using exec, so that we can see the names. Could be dangerous though, so I'm not sure.
def builder(original_class):
    attributes = [attr for attr in dir(original_class) if
                  not attr.startswith("_") and
                  attr in original_class.__dict__ and
                  not hasattr(original_class.__dict__[attr], "__call__")]

    original_init = original_class.__init__

    def __init__(self, **kwargs):
        for attr in attributes:
            try:
                self.__dict__[attr] = kwargs[attr]
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
