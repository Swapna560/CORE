def pronic(n):
    i=0
    while i*(i+1)<=n:
        if i*(i+1)==n:
            return True
        i+=1
    return False
n=int(input())
if pronic(n):
    print("Pronic Number")
else:
    print("Not Pronic Number")