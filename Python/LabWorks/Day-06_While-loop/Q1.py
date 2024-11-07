# Q.1)WAP to get factorial of a number using while loop.

# Take an integer input from the user
num = int(input("Enter a positive integer: "))

# Initialize variables
factorial = 1  # Start with factorial as 1
i = num  # Use i to iterate from num down to 1

# Calculate factorial using a while loop
while i > 1:  # Continue until i is greater than 1
    factorial *= i  # Multiply factorial by the current value of i
    i -= 1  # Decrement i by 1

# Display the result
print(f"The factorial of {num} is: {factorial}")
