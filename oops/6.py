# B3. Write a Counter class that starts at 0 and has an increment() method. Create one object and increment it 5 times,
# then print the count.


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


counter = Counter()

for i in range(5):
    counter.increment()

print(counter.count)


