# Write the same task — squaring only the even numbers from 1 to 10 — TWO
# ways: once using map + filter , and once using a list comprehension. In a
# comment, say which you find more readable and why.
# Tests: understanding both styles and when each fits.

square=list(map(lambda n:n**2,range(1,11)))

print(square)

even = list(filter(lambda n:n%2==0,square))

print(even) #return even result