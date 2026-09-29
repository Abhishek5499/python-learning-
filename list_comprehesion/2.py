# set comprehension

names = ['Ravi' , 'Amit', 'Sara', 'Neha','Ram']

# l = {i for i in names}

# print(l)


len_set ={len(ele) for ele in names}

print(len_set)

# out put :-
# {3, 4}


# if we want the lenght of all elements so we have to use list comprehension

len_list = [len(ele)  for ele in names ]

print(len_list)

# out put :-

# [4, 4, 4, 4, 3]

