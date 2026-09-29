num = [1,2,3,4,5,6,7,9]
for i in range(1,len(num)+1):
      for j in range(i) :

       print(num[j],end='')

      print()   

for i in range(5):        # Outer loop → 5 rows
    for j in range(5):    # Inner loop → 5 columns
        print("*", end="")
    print()               # Move to the next line


for i in range(5):
    for j in range(i):
        print('*',end='')  

    print()  


for i in range(1,6):
    print(i)    


for i in range(1,6):
    for j in range(1,11):
        print(f'{i} * {j}:',i*j)
    print()



h=[1,3,6]

print(h)

for i in range(30):
    print("*" , end="")
 