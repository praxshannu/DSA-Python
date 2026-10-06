n = int(input())
sum = 0
r = 0
while(n != 0):
    r = n % 10
    if(r %2==0):
        print(f"{r} -> is even ",r)
        sum = sum +1
    else:
        print(f"{r} -> is odd", r)
    n = n // 10
print ("count of even digits is " ,sum)
