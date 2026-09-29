# ex

def prod(num):

      p=1

      for i in num:
            p=p*i

      return p
num =[1,2,3,4,5]

print(prod(num))


#using reduce function 
#  syntax:

# first write  from functools import reduce

# reduce(function,collections)


from functools import reduce

pro = reduce(lambda a,b:a*b,num)

print(pro)