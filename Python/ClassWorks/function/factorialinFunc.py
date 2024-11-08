num=int(input("Enter Number: "))

def fac(num):
    i=1
    res=1
    while i<=num:
        res=res*i 
        i+=1
    return res    
       

print("Factorial Is: ",fac(num))    
