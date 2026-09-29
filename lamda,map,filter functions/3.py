# Using reduce() , find the sum of all numbers in [5, 10, 15, 20] . Then modify it
# to find the maximum instead.
# Hint: for max, reduce(lambda a, b: a if a > b else b, nums) .
from functools import reduce
num = [5,10,15,20]

sum =reduce(lambda a,b:a+b,num)

print(sum)

max = reduce(lambda a,b : a if a>b else b, num)

print(max)