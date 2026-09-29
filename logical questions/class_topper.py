l1 = [["Aman", 65], ["Riya", 91], ["Raju", 74], ["Priya", 88], ["Ali", 39]]

i = 0

topper_name = l1[0][0]
topper_marks = l1[0][1]

pass_count = 0
above_75_count = 0

while i < len(l1):

      name = l1[i][0]
      marks = l1[i][1]

      if marks > topper_marks:
            topper_marks = marks
            topper_name = name 

      if marks >= 40:

            pass_count += 1

      if marks >= 75:

            above_75_count += 1

      i += 1         


                          
print("Topper:", topper_name)
print("Topper Marks:", topper_marks)
print("Passed Students:", pass_count)
print("Students with 75 or more:", above_75_count)

      


          

      
