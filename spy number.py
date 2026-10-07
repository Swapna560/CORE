def spy(n):
    c=0
    p=1
    while n>0:
        r=n%10
        c+=r
        p*=r
        n=n//10
    if c==p:
        return True
    return False
n=int(input())
if spy(n):
    print("Spy Number")
else:
    print("Not Spy Number")