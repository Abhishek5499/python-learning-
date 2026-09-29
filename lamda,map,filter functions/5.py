# Given raw = ["$100", "$250", "$99"] , use map() to strip the $ and convert
# each to an integer. Then use filter() to keep only prices above 100.
# Hint: chain map then filter; p.replace("$", "") .

raw = ["$100", "$250", "$99"]

b = list(map(lambda p: p.replace("$",""),raw))

print(b)

price=list(filter(lambda n:n>"100",b))

print(price)
