# Write your favourite quote to a file quote.txt using with and write mode. Then
# read it back and print it.
# Hint: with open("quote.txt", "w") as f:

with open("quote.txt","w") as file:
      file.write("Good Things Take Time")


with open("quote.txt","r") as file:

      quotes=file.read()
      print(quotes)     