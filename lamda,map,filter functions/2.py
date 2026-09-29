# Given numbers 1 to 20, use filter() to keep only the odd numbers
# Hint: filter(lambda x: x % 2 != 0, range(1, 21))

# for num in range(1,20):

odd = list(filter(lambda n:n % 2 !=0,range(1,21)))

print(odd)