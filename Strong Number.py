def strong(n):
    t=n
    c=0
    while n>0:
        r=n%10
        f=1
        for i in range(1,r+1):
            f=f*i
        c+=f
        n=n//10
    if t==c:
        return True
    return False
n=int(input())
if strong(n):
    print("Strong Number")
else:
    print("no Strong NUmber")