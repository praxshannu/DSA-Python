n=[4,6,2,3,1,7,6,8,2,2,1,5,3,2]
k= int(input())
print(n,k)
su=0
max_sum=0
for i in range (len(n)-k):
    su=0
    print(i,"-i value and i is at ",n[i])
    for j in range(i,k+i):
        print(su," is added to with",n[j])
        su+=n[j]
    if su>max_sum:
        max_sum=su
        print(max_sum)
    else:
        print(max_sum," in else")
print(max_sum)
