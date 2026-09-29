# Open log.txt in append mode and add a new line each time the program runs.
# Run it 3 times and confirm all three lines are there (nothing erased).
# Hint: mode "a" .

 
with open("log.txt","a") as file:

      file.write("Where there is a will there is a way\n")
      file.write("The Best thing about time is , it changes\n")
      file.write("Life is a Game Play it\n")



 
