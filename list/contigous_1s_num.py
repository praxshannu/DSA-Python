
boo = True
n= int(input())
while boo:
    if n&1==1:
        n=n>>1
        if n == 0:
            break
    else:
        boo=False
print("the values contigious 1's",boo)
