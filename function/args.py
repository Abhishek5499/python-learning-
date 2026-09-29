# Write a function total(*args) that returns the sum of however many numbers
# are passed. Test it with 2 numbers, 5 numbers, and none.
def total(*args):

      sum=0

      for ele in args:
            sum=sum+ele
            # print(s)

      return sum

print(total(22,55,32,66,56 ))         