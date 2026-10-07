def sunny(n):
    i=0
    while i*i<=n+1:
        if i*i==n+1:
            return True
        i+=1
    return False
n=int(input())
if sunny(n):
    print("Sunny Number")
else:
    print("Not Sunny Number")