mylist=[12,20,3,4,5]
num=int(input('Enter Number to search in a list: '))
for i in mylist:
    if i==num:
        print('Present in list',i)
        break
    else:
        print('not prsetnt')
        break   