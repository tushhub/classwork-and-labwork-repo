# WAP to traverse a list of item and find particular item is present in the list or not

# Define a list of numbers
mylist = [12, 20, 3, 4, 5]

# Take user input for the number to search in the list
num = int(input('Enter Number to search in the list: '))

# Loop through each element in the list
for i in mylist:
    # Check if the current element is equal to the input number
    if i == num:
        print('Present in list:', i)   # Print message if number is found
        break                           # Exit the loop once number is found
    else:
        print('Not present')            # Print message if number is not found
        break                           # Exit the loop since we're only checking once
