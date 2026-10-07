def duck(n):
    if n==0:
        return False
    while n>0:
        r=n%10
        if r==0:
            return True
        n=n//10
    return False
n=int(input())
if duck(n):
    print("Duck number")
else:
    print("No duck number")