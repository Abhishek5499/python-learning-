# Write a function add3(a, b, c) that returns the sum of three numbers. Then,
# given a list nums = [4, 5, 6] , call add3 by unpacking the list with * .
# Hint: add3(*nums) .


# def add3(*nums):

#       return sum(nums)

# result =add3(4,5,6)


# print(result)

nums = [4, 5, 6]

def add3(a, b, c):
    return a + b + c

print(add3(*nums))


