
# Write a function describe(**kwargs) that prints "name is Amit" , "age is 21" ,
# etc., for whatever keyword arguments are passed.
# Hint: loop kwargs.items() .


def describe(**kwargs):

     for key,value in kwargs.items():
          print(f'{key} is {value}')



describe(name = "Amit",age = 21)