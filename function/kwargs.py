# Write a function profile(**kwargs) that prints every key-value pair passed to it
# as "key: value" . Call it with a few named arguments.
# Uses: **kwargs + .items()


# def profile(**kwargs):

#       return kwargs


# info = profile(name="abhi",age=23,roll=23)

# print(info)



def profile(**kwargs):

      for key,value in kwargs.items():

            print(f'{key} : {value}')

profile(name="abhi",age=23,roll=23)          