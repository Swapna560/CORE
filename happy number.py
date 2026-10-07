def happy(n):
    while n!=1 and n!=4:
        c=0
        while n>0:
            r=n%10
            c+=r*r
            n=n//10
        n=c
    if n==1:
        return True
    return False
n=int(input())
if happy(n):
    print("Happy NUmber")
else:
    print("No happy number")