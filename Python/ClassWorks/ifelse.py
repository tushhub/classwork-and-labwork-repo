age = int(input("Enter Child's Age: "))

if age >= 6:
    print("Eligible for Sr. kg")
elif age >= 4:
    print("Eligible for Jr. kg")
elif age > 3:
    print("Eligible for Nursery")
else:
    print("Eligible for Playgroup")

for i in range(1,21):
    if(i%2==0):
        print("Even Numbers: ",i)
