# Q.3)WAP to check whether person can vote or not using function

# Get age from the user
age = int(input("Enter Your Age: "))

# Function to check if the user is eligible to vote
def CheckAge(age):
    if age >= 18:
        print("You Are Eligible For Voting.")   # Print if age is 18 or above
    else:
        print("You Are Not Eligible For Voting.") # Print if age is below 18

# Call the function with the entered age
CheckAge(age)
