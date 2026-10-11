a= [4,6,2,3,1,7,6,8,3,2,1,1,5,3,8,2]
l=0
r=0
k=14
s=0
ms=0
length=len(a)
while r<length:
    if s<=k:
        s+=a[r]
        r+=1
        if r-l >ms:
            ms=r-l-1
    else:
        while s>k:
            s-=a[l]
            l+=1
print(ms)
""" or 
while r< len(a):
    s=a+s[r]
    while s> k:
        s=s-a[l]
        l=l+1
    mx=max(mx,r-l+1)
    r=r+1
print(mx)
"""


