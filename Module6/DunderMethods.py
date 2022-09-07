# Methods having double underscores

class CoolClass:
    def __init__(self, value):
        self.value = value
    def __add__(self, val):
        return self.value - val


# More examples of Dunder methods:
# '__abs__', '__add__', '__and__', '__bool__',
#  '__ceil__', '__class__', '__delattr__', '__dir__',
#  '__divmod__', '__doc__', '__eq__', '__float__',
#  '__floor__', '__floordiv__', '__format__', '__ge__', 
# '__getattribute__', '__getnewargs__', '__gt__', '__hash__',
#  '__index__', '__init__', '__init_subclass__', '__int__',
#  '__invert__', '__le__', '__lshift__', '__lt__', '__mod__',
#  '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', 
# '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
#  '__rmul__', '__ror__', '__round__', '__rpow__', 
# '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
#  '__rxor__', '__setattr__', '__sizeof__',
#  '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__'