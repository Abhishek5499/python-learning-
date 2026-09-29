# #Creat a string with your name. Print its length and data type.

# name = "Abhishek"
# print(type(name))
# print(len(name))

a =[1,4,6,4,8,9,34,5,4]

large = a[0]

slarge = a[0]

for i in (a) :
      if i > large:
            slarge = large
            large = i
      elif i > slarge and i <large :
            slarge = i



print(slarge)       

           