def neon(n):
    c=0
    s=n*n
    t=n
    while s>0:
        r=s%10
        c+=r
        s=s//10
    if c==t:
        return True
    return False
n=int(input())
if neon(n):
    print("Neon Number")
else:
    print("Not Neon Number")