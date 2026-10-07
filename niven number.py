def niven(n):
    c=0
    t=n
    while n>0:
        r=n%10
        c+=r
        n=n//10
    if t%c==0:
        return True
    return False
n=int(input())
if niven(n):
    print("Niven Number")
else:
    print("Not Niven NUmber")