## Higher Order Functions
def square(number):
    return number**2

def cube(number):
    return number**3

def process_value(function, value):
    result = function(value)
    return result

## Nested functions
def modify(value):
    def increase(value):
        return value + 1
    return increase(value)

def myfunc():
    a = 3
    def mynestedfunc():
        nonlocal a
        a = 5
        print(f'Nested value {a}')
    mynestedfunc()
    print(f'Outside Func {a}')

## Closure Example
def main_function(x):
    def nested_func():
        print(f'Nested Function: {x}')
    return nested_func

# value = main_function(3)
# Even if main_function is deleted, we can still call value()
# Also, we can check the cell contents of the closure using __closure__ attribute:
# value.__closure__[0].cell_content 