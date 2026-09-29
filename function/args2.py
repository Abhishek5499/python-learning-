# Write a function multiply(*args) that returns the product of all numbers passed.
# multiply(2, 3, 4) → 24.
# Hint: start a result at 1, loop over args , multiply each

def multiply(*args):

      mul =1

      for ele in args:

            mul=mul*ele

      return mul

print(multiply(2,3,4))      