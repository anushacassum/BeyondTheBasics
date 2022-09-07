import timeit

x = 'Hello'
y = 'I am 100 years old'

############ LETS TIME THEM #######


print('Technique 1: x + " " + y') 


option1 = timeit.timeit("""
x = 'Hello'
y = 'I am 100 years old'
x + " " + y
""")

print(option1)
##################################

print('Technique 2: " ".join((x, y))')  # 

option2 = timeit.timeit("""
x = 'Hello'
y = 'I am 100 years old'
" ".join((x, y))
""")

print(option2)


##################################

print('Technique 3: "%s %s" % (x, y)')  # 

option3 = timeit.timeit("""
x = 'Hello'
y = 'I am 100 years old'
"%s %s" % (x, y)
""")
print(option3)

##################################

print('Technique 4: "{} {}".format(x, y)')  # 

option4 = timeit.timeit("""
x = 'Hello'
y = 'I am 100 years old'
"{} {}".format(x, y)
""")
print(option4)

##################################

print('Technique 5: f"{x} {y}"')  # 


option5 = timeit.timeit("""
x = 'Hello'
y = 'I am 100 years old'
f"{x} I am {y} years old"
""")

print(option5)

##################################
