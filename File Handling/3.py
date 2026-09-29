# Ask the user for a filename and print its contents. Use try/except so a missing file
# prints "File not found" instead of crashing.
# Uses: with + FileNotFoundError

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found")