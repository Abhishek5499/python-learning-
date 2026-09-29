# Given a list of words, use reduce() to find the longest word — without max() .
# ["hi", "python", "lambda", "ok"] → "python" .
# Tests: custom combine step; reduce(lambda a, b: a if len(a) >= len(b) else b,
# words) .

from functools import reduce

words =["hi", "python", "lambda", "ok"]  

long = reduce(lambda a,b:a if len(a)>=len(b) else b,words)

print(long)