a=[6,5,8,3,4,2,2,34,6]
b=set(a)
for i in b:
    count = 0
    for j in range(len(a)):
        if(i==a[j]):
            count+=1  
    print(i,",",count)
    print()
