# . Sum of the Series 1 + 4 + 9 + 16 + ...
# Read n and calculate the sum of the first n square numbers: 1² + 2² + 3² + ... + n².

num = 4
sum = 0

for i in range(1,num+1):
      square = i*i
      sum = sum + square
print(sum)      


