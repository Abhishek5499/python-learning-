 
with open("log.txt","r") as file:

      content = file.readlines()

      print(content) 

print("\n")

print("-------------------------------------------------------")

file1 =open('log.txt','r')

for line in file1:

      print(line.strip())

file1.close()