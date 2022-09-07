## DECORATORS
## Apply a chain of decorators as shown below

# @decoratorB
# @decoratorA
# def myfunction(some_string):
# ...return print(some_string.lower())
# ...
#
# To produce the required output given below!
"""
>>> myfunction('I love Python!')
I LOVE PYTHON!
I love python!
i love python!
"""


def myfunction(some_string):
    return print(some_string.lower())