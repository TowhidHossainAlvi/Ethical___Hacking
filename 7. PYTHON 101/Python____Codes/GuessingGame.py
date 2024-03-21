def result(e,f):
    if e==f:
        return None
    elif e=='r':
        if f=='p':
            return True
        elif  f=='s':
            return False
    elif e=='p':
        if f=='s':
            return True
        elif f=='r':
            return False
    elif e=='s':
        if f=='r':
            return True
        elif f=='p':
            return False


import random
a=random.randint(1, 3)
if a==1:
    c='r'
elif a==2:
    c='p'
elif a==3:
    c='s'

b=input("Enter your choice among 1,2 or 3 : ")
d=result(c,b)           
if d==None:
    print("Tie")
elif d:
    print("Win") 
else:
    print("Lost")      
print(f"computer choose {c}")
print(f"you choose {b}")     
