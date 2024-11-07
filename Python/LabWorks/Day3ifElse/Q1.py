# Q.1 Using input function take two numbers and then swap the numbers
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

# Swapping logic using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Printing the swapped values
print("After Swapping, num1:", num1)
print("After Swapping, num2:", num2)
