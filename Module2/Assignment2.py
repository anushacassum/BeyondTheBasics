### ASSIGNMENT 2 ###
"""
Modify the function below such that
its able to take a variable number of arguments.

Caution: Python wants us to always put keyword 
arguments after positional arguments!
"""

def cooking(name, utensils, ingrediants):
    """
    This function 'cooks'.
    :param name: Name of the receipe
    :param required: Names of the required utensils needed.
    :param ingrediants: Names of ingrediants
    """
    print(f"### Lets cook {name}!### \n")
    print("Check to see that you have all the following utensils:")
    print(utensils)
    print(f"\nMost importantly, check if the following ingrediants with the specified quantities are present")
    print(f"{ingrediants}")
    print(f"Mix them all up and enjoy!")


cooking('Khaousay', 'Plate', 'Noodle')

"""
You should be able to call the function above 
with the following result:

### Lets cook Khaousay!### 

Check to see that you have all the following utensils:
Plate
Spoon
Bowl

Most importantly, check if the following ingrediants with the specified quantities are present
1packet of Noodles
1packet of CoconutCurry
1/2 kg of Chicken
1tbsp of Spices
Mix them all up and enjoy!
"""