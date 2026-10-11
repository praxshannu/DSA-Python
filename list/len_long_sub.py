a=[4,6,2,3,1,7,6,8,3,2,1,1,5,3,8,2]
mlen=0
k=14
max=0
for i in range(len(a)):
    sum=0
    for j in range(i,len(a)):
        sum+=a[j]
        if sum <=k:
            if(j-1-i>max):
                max=j-1-i
                print(sum)
print(max)
