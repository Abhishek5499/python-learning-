# dictionary comprehension

word = ['hi', 'python', 'set']

length =({ele:len(ele)  for ele in word  })

print(length)

print(type(length))