# Q.2)WAP to get factorial of a number


# Get input from the user
num = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1

# Calculate factorial using a for loop
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
