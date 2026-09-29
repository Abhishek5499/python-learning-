def factorial(num):

      fact = 1
      n1 = num 

      while num > 0:

            fact = fact * num

            num -= 1
      print(f'Factorial of {n1} : {fact}')     
# factorial(3)      

def sum_digits(num):

      sum = 0
      n2 = num

      while num > 0:

            digit = num % 10

            sum = digit + sum

            num = num // 10

      print(f'Sum of {n2} is : {sum}')

# sum_digits(123)
