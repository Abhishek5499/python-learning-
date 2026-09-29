# write a program take user input as number check whether the number is prime n of not

num = int(input("Enter the number: "))

count = 0

for i in range(1, num + 1):

    if num % i == 0:
        count = count + 1

if count == 2:
    print(f"{num} is a prime number")

else:
    print(f"{num} is not a prime number")

 #end   