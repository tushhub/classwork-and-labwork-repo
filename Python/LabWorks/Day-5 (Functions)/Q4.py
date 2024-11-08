# Q.4)WAP to get table of a number using function

# Get a number from the user
num = int(input("Enter Number To get Table: "))

# Function to generate the multiplication table
def table(num):
    result = []  # Initialize an empty list to store each line of the table
    for i in range(1, 11):
        res = num * i  # Calculate the result of num multiplied by i
        result.append(f"{num} x {i} = {res}")  # Format and add the line to the list
    return result  # Return the complete list of table lines

# Print each line of the table
for line in table(num):
    print(line)
