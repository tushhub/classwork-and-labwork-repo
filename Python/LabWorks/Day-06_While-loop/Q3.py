# Q.3)Write a while loop to calculate the sum of digits of a given number.

# Take an integer input from the user
number = int(input("Enter a number: "))

# Initialize the sum of digits to 0
sum_of_digits = 0

# Use the absolute value to handle negative numbers
number = abs(number)

# Calculate the sum of digits using a while loop
while number > 0:
    digit = number % 10  # Get the last digit
    sum_of_digits += digit  # Add the digit to the sum
    number //= 10  # Remove the last digit from the number

# Display the result
print("Sum of digits is:", sum_of_digits)
