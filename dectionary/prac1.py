# # Answer
# student = {"name": "Rahul", "age": 20}

# key = input("Enter key: ")

# if key in student:
#     print("Key exists")
# else:
#     print("Key not found")

# Answer
# student = {"name": "Rahul", "age": 20, "marks": 80}

# print(len(student))
# Answer
# Answer
# marks = {"math": 80, "science": 70, "english": 90}

# total = 0
# for value in marks.values():
#     total += value

# print(total)
# Answer
# Answer
# Answer
marks = {"math": 85, "science": 92, "english": 78}

min_marks = 100
subject = ''

for key , value in marks.items():
    if value < min_marks:
        min_marks = value
        subject = key

print(subject,min_marks)        