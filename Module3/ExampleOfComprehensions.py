## Examples of Comprehensions

## List Comprehensions
numbers = [1,2,3,4,5,6,7,8,9,0]
even_numbers = []
for even_no in numbers:
    if even_no % 2 == 0:
        even_numbers.append(even_no)    

# In list comprehension the above for loop can be written as:
even_numbers = [even_no for even_no in numbers if even_no % 2 == 0]


## Dictionary Comprehensions
people = {'Sam': 10, 'Max':5, 'Anna': 15, 'Ben': 25}
adults_after_5yrs = {}

for key,value in people.items():
    if (value + 5) >= 18:
        adults_after_5yrs.update({key:value})

# In distionary comprehension the above for loop can be written as:
adults_after_5yrs = {key:value for key,value in people.items() if (value + 5)>=18}


## Set Comprehensions
number_list = [1, 1, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8]
non_duplicate_set = set()

for num in number_list:
    if num % 2 == 0:
        non_duplicate_set.add(num)

# In set comprehension the above for loop can be written as:
non_duplicate_set = {num for num in number_list if num % 2 == 0}
