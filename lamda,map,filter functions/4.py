# Given names = ["Amit", "Neha", "Ravi", "Sara"] , sort them by their last letter
# using sorted() with a lambda key.
# Hint: sorted(names, key=lambda n: n[-1])

names = ["Amit", "Neha", "Ravi", "Sara"]

sortname=sorted(names, key=lambda n:n[-1])

print(sortname)