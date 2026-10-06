n = int(input())
sum = 0
r = 0
i=1
while(n != 0):
    r = n % 10
    sum = sum + r**i
    n = n // 10
    i=i+1
    print ("sum is " ,sum)
print ( "final sum is " , sum )

