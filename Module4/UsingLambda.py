## EXAMPLES OF USING LAMBDA

## Map with Lambda
numbers = [1,5,7,3,9]
plus_one = list(map(lambda x: x+1, numbers))

## Filter with Lambda
numbers = [1,2,3,4,5,6,7,8,9]
odd = list(filter(lambda x: x%2 != 0, numbers))

## Reduce with Lambda
numbers = [2,4,6,73,6,8]
import functools
sum_of_all = functools.reduce(lambda x,y: x+y, numbers)