### Static Methods:
# Also a method that is bound to the class and not the object of the class.
# Can’t access or modify the class state.
# Present in a class because it makes sense for the method to be present in class.

class Pet():
  state = 'alive'
  def __init__(self, species, name):
    self.species = species
    self.name = name
  def describe_attributes(self):
    print(f'My pet is a {self.species}. Its name is {self.name}')
  @staticmethod
  def is_alive(state):
    print(f'My pet is {state}')
  def pet_alive(self):
    print(f'My pet is {self.state}')
