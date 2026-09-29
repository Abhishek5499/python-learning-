# Write a function how_many(*args) that returns how many arguments were passed.
# Test with different counts.
# Hint: len(args) .

# def how_many(*args):

#       count=0

#       for i in args:
#             count=count+1

#       return count

# print(how_many(2,3,45,6,8,4,5,2,3))     


def how_many(*args):

      return len(args)

print(how_many(2,3,45,6,8,4,5,2,3)) 
