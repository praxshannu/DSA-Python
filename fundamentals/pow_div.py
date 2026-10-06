n = int(input())
sum = 0
r = 0
while(n != 0):
    r = n % 10
    sum = sum + r**2
    n = n // 10
    print ("sum is " ,sum)
print ( "final sum is " , sum )

