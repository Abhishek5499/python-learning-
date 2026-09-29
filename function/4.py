# Write a function biggest(a, b, c) that returns the largest of three numbers —
# without using max() .


def biggest(a,b,c):
      if a>b:

            if a>c:
                 return a
            else :

                  return c

      else :
            if b>c:
                  return b
            else:
                  return c     


result =biggest(5,10,7)     

print(result)