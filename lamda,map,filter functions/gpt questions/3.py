nums = [4, 7, 12, 15, 20, 25, 30, 3]

even=filter(lambda n:n%2==0 and n>10 , nums)

sq=list(map(lambda n:n**2,even))
print(sq)
from functools import reduce

result =reduce(lambda a,b:a+b , sq)

print(result)