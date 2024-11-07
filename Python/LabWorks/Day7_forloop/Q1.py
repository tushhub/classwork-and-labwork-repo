''''
Q.1)WAP to print triangular  pattern

*                         1                         1

* *                      1 2                      2 2 

* * *                   1 2 3                   3 3 3

* * * *                1 2 3 4                4 4 4 4

'''

# First pattern: Print a right triangle of asterisks
for i in range(1, 5):            # Outer loop for each row
    for j in range(1, i + 1):     # Inner loop to print '*' in each row
        print('*', end=" ")       # Print '*' without moving to the next line
    print()                       # Move to the next line after each row

# Second pattern: Print a right triangle of numbers, increasing in each row
for i in range(1, 5):            # Outer loop for each row
    for j in range(1, i + 1):     # Inner loop to print numbers from 1 to i in each row
        print(j, end=" ")         # Print the number without moving to the next line
    print()                       # Move to the next line after each row

# Third pattern: Print a right triangle of repeating row numbers
for i in range(1, 5):            # Outer loop for each row
    for j in range(1, i + 1):     # Inner loop to print the row number i, i times
        print(i, end=" ")         # Print the row number without moving to the next line
    print()                       # Move to the next line after each row
