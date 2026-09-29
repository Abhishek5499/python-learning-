#count duplicates number in the list

num = [1,2,4,6,5,4,2,3,7,3]

dup =[]


for i in num:
      count=0
      for j in num:
            if i==j:
             count=count+1
      if count>1 and i not in dup:
          dup.append(i)
print(dup)

                      
  