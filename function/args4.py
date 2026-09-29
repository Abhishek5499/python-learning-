# Write a function biggest(*args) that returns the largest number passed —
# without using max() . Handle the empty case by returning None .
# Hint: "best so far" pattern from #11.2, looping over args .



def biggest(*args):

      largest=args[0]

      for ele in args:

            if ele>largest:
                  largest=ele

      print(largest)      

biggest(77,4,33,55,6)
