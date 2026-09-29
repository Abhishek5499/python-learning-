a = int(input('Enter the first number :'))
b = int(input('Enter the second number :'))
c = int(input('Enter the third number :'))


if a>b and a>c:
      print(f"Greatest between {a}, {b} and {c} is {a}")
elif b > a and b > c:
    print(f"Greatest between {a}, {b} and {c} is {b}")
else:
  print(f"Greatest between {a}, {b} and {c} is {c}")