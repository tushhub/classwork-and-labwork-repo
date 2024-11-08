# Q.1)WAP to get factorial of a number using function

# Get input from the user
num = int(input("Enter Number: "))

# Function to calculate factorial
def fac(num):
    res = 1      # Initialize result as 1
    i = 1        # Start counter at 1
    while i <= num:
        res *= i # Multiply res by i
        i += 1   # Increment i
    return res   # Return factorial result

# Display the result
print("Factorial Is:", fac(num))

