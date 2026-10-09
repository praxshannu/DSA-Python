h=[1,8,6,2,5,4,8,3,7]
l=0
r=len(h)-1
ls=[]
#i,h[i] ---> solution max water is i* h[i]
# it could be distance of between the indices too * max
while l<r:
    ls.append(r-l * max(h))
    l+=1
    r-=1
print(max(ls))
