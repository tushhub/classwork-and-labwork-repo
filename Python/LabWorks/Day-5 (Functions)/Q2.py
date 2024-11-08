# Q.2)WAP to find maximum among two number

# Get two numbers from the user
num1 = int(input("Enter Num 1: "))
num2 = int(input("Enter Num 2: "))

# Function to find the maximum of two numbers
def MaxNum(num1, num2):
    if num1 > num2:
        print("Maximum Number Is:", num1)   # If num1 is greater, print num1
    elif num1 < num2:
        print("Maximum Number Is:", num2)   # If num2 is greater, print num2
    else:
        print("Both Numbers Are the Same.") # If equal, print they're the same

# Call the function with the input numbers
MaxNum(num1, num2)
