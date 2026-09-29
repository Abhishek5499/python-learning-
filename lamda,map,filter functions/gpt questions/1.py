nums = [12, 5, 8, 21, 30, 7, 14, 3]


even =list (filter(lambda n:n%2==0 and n>10,nums))

from functools import reduce

pro=reduce(lambda a,b:a*b,even)

print(pro)