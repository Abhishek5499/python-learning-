# Take total seconds as input from the user
total_seconds = int(input("Enter total seconds: "))

# Calculate hours, remaining seconds, minutes, and final seconds
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Display the result
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")