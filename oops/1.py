# S1. Build a Student class with name and marks. Add a method has_passed() that returns True if marks ≥ 40.

class student:

      def __init__(self,name,marks):

            self.name=name
            self.marks=marks

      def has_passed(self):


            if self.marks>=40 :

              return True

            else :
                 return False

result = student('Abhishek',56) 

print(result.has_passed())


            

      