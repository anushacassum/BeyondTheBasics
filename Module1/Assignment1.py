### ASSIGNMENT 1: GREET OUR USERS ###

""" Write a function that takes the name of the user 
and greets them in return. 
Greet with surname only if surname is provided. 
Ensure that the first letter of the name of the individual is always capitalised.
Constraint: The function should not be longer than one line"""

def greetings(name):
	### Your one liner code ##
	return name

if __name__ == '__main__':
	print(greetings('albert einstein')) ## "Hello Einstein!"
	print(greetings('anusha')) ## "Hello Anusha!"
