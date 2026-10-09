a=[1,0,1,0,1,0,2,1,0,1,2]          
s=0
m=0
e=len(a)-1
while m<=e:
    if a[m] == 2:
        a[m],a[e]=a[e],a[m]
        e-=1
        print(s,m,e,a)
    elif a[m]==0:
        a[m],a[s]=a[s],a[m]
        s+=1
        m+=1
        print(s,m,e,a)
    else:
        m+=1 
        print(s,m,e,a)
        
