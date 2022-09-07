# An object is called iterable if we can get an iterator from it. 
# Most built-in containers in Python like: list, tuple, string etc. are iterables.

class Count:
    """Iterator that counts upward forever."""
    def __init__(self, start=0):
        self.num = start
    def __iter__(self):
        return self
    def __next__(self):
        num = self.num
        if self.num == 10:
            raise StopIteration
        self.num += 1
        return num



# TreyHunter: https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/