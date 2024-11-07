# Q.2)Write a while loop that counts the number of digits in a given number

num = int(input("Enter a Number: "))  # Take an integer input from the user
count = 0  # Initialize the count of digits to 0

while num != 0:  # Continue the loop until num is not 0
    num //= 10  # Remove the last digit from the number
    count += 1  # Increment the count of digits

print("Number of digits is:", count)  # Display the total number of digits
