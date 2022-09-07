## Using Args ##

def multiply(*args):
    result = 1
    for each in args:
        result = result * each
    return result


def favourite_gift(*args):
    print(f"{args[0]} is my favourite gift") 
    print(type(args))


## Using Kwargs

def introduction(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")