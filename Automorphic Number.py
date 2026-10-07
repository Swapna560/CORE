def Automorphic(n):
    p=1
    t=n
    s=n*n
    while n>0:
        r=n%10
        p*=10
        n=n//10
    if s%p==t:
        return True
    return False
n=int(input())
if Automorphic(n):
    print("Automorphic Number")
else:
    print("No Automorphic Number")