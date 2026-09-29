# Write a function grade(marks) that returns "A", "B", "C", or "Fail" based on the
# marks (your own cutoffs). Test it with a few values.

def grade(marks):

      if marks>70:
            return "A"

      elif marks>65:
            return "B"

      elif marks> 55:
            return "C"

      else:
            return "Fail"


print(grade(55))      
print(grade(60))      
print(grade(90))      
print(grade(30))      
                     







