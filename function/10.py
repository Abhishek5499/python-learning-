
# Write code with a global x = "global" and a function that creates a local x =
# "local" and prints it. Outside the function, print x too. In a comment, explain
# why the two prints differ.


x = 33

def sum():

      x=22

      print(x)      # Local x, so it prints 22

sum()
print(x)       # Global x, so it prints 33