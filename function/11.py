# Write a function summary(nums) that returns the minimum, maximum, AND
# average — three values as a tuple. Add a docstring. Unpack all three and print
# them.
# Hint: return min(nums), max(nums), sum(nums)/len(nums)

def s(num):

      ''' Extract max ,mim,avg of given number'''

      return max(num),min(num),sum(num)/len(num) 


max,min,avg=s([22,44,23,56,7])

print('Max',max)
print('Min',min)
print('avg',avg)
print(s.__doc__)

