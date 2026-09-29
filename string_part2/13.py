#  Split the CSV string 'Rajeev,25,Varanasi,Python' into a list and print each value on a new line

a = 'Rajeev,25,Varanasi,Python'

print(*a.split(","), sep="\n")

# The * is called the unpacking operator.

print(*['Rajeev', '25', 'Varanasi', 'Python'])

# output
# print(*['Rajeev', '25', 'Varanasi', 'Python'])


# sep="\n" do?

# sep means separator.


