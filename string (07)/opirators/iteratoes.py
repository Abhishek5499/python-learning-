student = {
    "name":"Abhi",
    "age":22
}

it = iter(student.values())

print(next(it))
 
# iterators to list 
num = [10,20,30]
a = iter(num)

print(list(a))
