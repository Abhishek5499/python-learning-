# list and set comprihension

l1 = [i*i for i in range(1,10) if i%2==0]

print(l1)

list =['raju','bheem','bhav']

print(len(list))

# print(list(list[0])) incorrect syntax.

len = [len(ele) for ele in list]

# len2 = {len(ele) for ele in list}

print(len)

# print(len2):