a=[5,6,4,0,7,0,0,3,0,0,6,0]
tem=0
for i in range(len(a)):
    if a[i]==0:
        for j in range(i+1,len(a)):
            if(a[j]!=0):
                tem= a[j]
                a[j]=a[i]
                a[i]=tem
                break
print(a)
