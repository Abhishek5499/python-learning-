# Write a function interest(principal, rate, years) that returns the simple
# interest ( P * R * T / 100 ). Give rate a default of 5. Call it once using the
# default and once overriding it.

def interest(p,t,r=5):
      return (p*r*t/100)

result = interest(103,4)
result2=interest(103,4,9)

print(result,result2)