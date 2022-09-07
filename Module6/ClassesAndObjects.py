class Pet():
  state = 'alive'
  def __init__(self, species, name):
    self.species = species
    self.name = name
  def describe_attributes(self):
    print(f'My pet is a {self.species}. Its name is {self.name}')
  @classmethod
  def is_alive(cls):
    print(f'My pet is {cls.state}')
  def pet_alive(self):
    print(f'My pet is {self.state}')
