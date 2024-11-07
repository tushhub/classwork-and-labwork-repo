# Q.4)Create a while loop to print the Fibonacci series up to n terms.

# Take the number of terms as input from the user
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1

# Initialize a counter to keep track of the number of terms printed
count = 0

print("Fibonacci series up to", n, "terms:")

# Use a while loop to generate the Fibonacci series
while count < n:
    print(a, end=' ')  # Print the current term
    # Update values for the next term
    a, b = b, a + b  # Set a to b and b to the next term in the series (a + b)
    count += 1  # Increment the counter

print()  # Print a newline at the end
