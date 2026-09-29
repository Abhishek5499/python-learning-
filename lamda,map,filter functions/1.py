# Given words = ["python", "lambda", "map"] , use map() to build a list of the
# words in UPPERCASE.
# Hint: map(lambda w: w.upper(), words)

words = ["python", "lambda", "map"] 

cap=list(map(lambda w:w.upper(),words ))
print(cap)