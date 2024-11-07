n = int(input("Enter a number: "))
original_n = n  
re = 0

while n > 0:
    rem = n % 10
    re = re * 10 + rem
    n = n // 10

if re == original_n:
    print('is palindrome')
else:
    print('not a palindrome')
