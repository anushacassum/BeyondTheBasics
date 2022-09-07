class Food():
    edible = True
    _calories = 100    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __add__(self, object):
        # example of a Dunder method
        return self.name + ' ' + object.name
    def describe(self):
      print(f'{self.name} is a food item.')


## Inheritance
"""
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
"""

class JunkFood(Food):
    pass


## Polymorphism
# Polymorphism means the same function name (but different signatures) being used for different types.
## Overriding vs Overloading (Not supported by Python by default):
class HealthyFood(Food):
    def describe(self):
      print(f'{self.name} is a healthy food item!')
    

## Encapsulation
# The concept of bundling data and methods within a single unit.
# Protected variables VS Private Variables
class Person():
  age = 0
  height = '5ft'
  _weight = '50kg'
  __diseases = 'Asthma'
  def __init__(self, name):
    self.name = name
  def access_protected(self):
    print(f'Weight is {self._weight}')
  def access_private(self):
    print(f'Medical conditions include: {self.__diseases}')



## Abstraction
# Process of handling complexity by hiding unnecessary information from the user.
from abc import abstractmethod
class Food():
    edible = True
    _calories = 100    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __add__(self, object):
        # example of a Dunder method
        return self.name + ' ' + object.name
    def describe(self):
      print(f'{self.name} is a food item.')
    @abstractmethod
    def we_like_it(self):
      pass
