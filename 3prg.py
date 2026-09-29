num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

choice = input("Enter your choice + - \ * :")
               
if choice =="+":
   print(f" sum of {num1} and {num2} is : {num1+num2}")

elif choice =="-":
     print(f"The sub of two number is : {num1-num2}")

elif choice == "*":
     print(f"the mult of two number is : {num1*num2}")

else :
     print("invalid choice /n Choose valid choice")
     



