num = int(input("Enter the number :"))
prod = 1

while num>0:
      digit = num%10

      prod =prod*digit
      num = num//10

print(prod)      