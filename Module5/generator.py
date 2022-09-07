## Example of a generator function
def get_sequence_upto(x):
    for i in range(x):
        yield i

"""
 Produces a generator Object eg:
 <generator object get_sequence_upto at 0x7f55e7ca3b30>
"""
# Using Generators

# Easy to implement compared to OOP way of generating iterators
def Count():
    for i in range(10):
        yield i+1


# Pipelining generators
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def cube(numbers):
    for num in numbers:
        yield num**3

print(sum(cube(fibonacci_numbers(5))))