a=[6,5,8,3,4,2,8,7,9,9,8,6,2,3,2,4]
for i in range(len(a)):
    count = 0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            count+=1
    print(a[i],"-",count)

