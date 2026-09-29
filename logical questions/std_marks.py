l1 =[]

for i in range (1,7):
      marks =int(input(f"Enter the marks of stud {i} :"))

      l1.append(marks)
total = sum(l1)
avg = total/len(l1)
height_marks = max(l1)

print(total,"\n",avg,"\n",height_marks )

l2 = []
i=0
while i<len(l1):

      if l1[i]>=40:
          l2.append('Pass')
      else :
            l2.append('Fail')
      i +=1      
print(l2)            
   
      
