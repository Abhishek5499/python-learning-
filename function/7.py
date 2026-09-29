
# Write a function stats(nums) that returns BOTH the sum and the average as a
# tuple. Call it and unpack the result into two variables in one line, then print them

def stats(nums):
      return sum(nums),(sum(nums)/len(nums))

sum_avg=stats([10,37,44])

# print('sum:',sum)
# print('avg:',avg)

print(sum_avg)