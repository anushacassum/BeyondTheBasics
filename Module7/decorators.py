# Creating decorators (Functions without args/kwargs)

def func():
    print('This is my function')


def surround_it(func):
    def inner_func():
        print('Surrounding this function..')
        func()
        print('...surrounding this function!')
        return
    return inner_func

func = surround_it(func)

@surround_it
def func():
    print('This is my function')


###########################################
# Creating decorators (Functions with args/kwargs)

def subtract(func):
    def absolute_value(*args, **kwargs):
        if args[0] < args[1]:
            print("Difference cannot be negative!")
            return
        return func(args[0], args[1])
    return absolute_value

def difference(A,B):
    return A - B

####################################

def main():
    print('Main Function')


def asterik(func):
    def inner_func():
        print('**************************')
        func()
        print('**************************')
        return
    return inner_func

def dollar(func):
    def inner_func():
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        func()
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        return
    return inner_func

# Chaining decorators
@asterik
@dollar
def main():
    print('Main Function')

@dollar
@asterik
def main():
    print('Main Function')
