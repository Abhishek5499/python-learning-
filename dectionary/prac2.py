marks = {"math": 85, "science": 92, "english": 78}

min_marks = 100
max_marks = 0
subject = ''

for key , value in marks.items():
     
     if  value < min_marks:
      min_marks = value
      subject = key

     if value > max_marks:
      max_marks = value
      subject = key

print("Max",key,value)
print("Min"key,value)




