data = [
    {"name": "Alice", "scores": [85, 92, 78, 90]},
    {"name": "Bob", "scores": [70, 88, 95, 60]},
    {"name": "Charlie", "scores": [90, 91, 89, 94]},
    {"name": "David", "scores": [55, 65, 72, 58]},
    {"name": "Eva", "scores": [95, 98, 92, 96]}
]


filtered = filter(lambda student:
                  sum(student['scores'])/len(student['scores'])>=85
                  and min(student['scores'])>=75,data)

result=map(lambda student:student["name"],filtered)

print(list(result))