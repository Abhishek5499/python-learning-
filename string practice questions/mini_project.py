a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))

choice = int(input('''
 1. Addition
 2.substrsction
 3.multiplication
 4.division
Enter your choice :'''))

if choice == 1 :
      print(f"Addition of {a} and {b} is :",a+b)

elif choice == 2:
      print(f"Substraction of {a} and {b} is :",a-b)  

elif choice == 3:
      print(f"multiplication of {a} and {b} is :",a*b)

elif choice == 4:
      print("Division of {} and {} is " .format(a,b),a/b)

else :
      print("Enter the valid choice !")      