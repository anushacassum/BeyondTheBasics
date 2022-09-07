### F strings ###

name = "Anusha"
course = 'Beyond the Basics'
print(f"Hello, I'm {name}. We're learning {course}.")


### Call functions through fstrings
animal = 'CAT'
print(f"{animal.lower()}")


### Conditional Formatting
import datetime
time_today = datetime.datetime.now()
print(f'Result: {time_today:{"Weekday" if time_today.weekday() < 5 else "Weekend!"}}')


### Use f strings in classes
class Person():
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    
    def description(self):
        return f"{self.name} is {self.age} years old, and likes {self.hobby}"
    
