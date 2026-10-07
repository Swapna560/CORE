def technumber(n):
    t=n
    c=0
    while n>0:
        r=n%10
        c+=1
        n=n//10
    if c%2!=0:
        return False
    p=10**(c//2)
    first=t//p
    second=t%p
    return (first+second)**2==t
n=int(input())
if technumber(n):
    print("Yes")
else:
    print("No")