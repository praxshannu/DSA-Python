n=[4,6,2,3,1,7,6,8,2,2,1,5,3,2]
k= int(input())
print(n,k)
su=0
max_sum=0
for i in range(k):
    su+=n[i]
for i in range (k,len(n)-k):
    su+=n[i]-n[k-i]
    if su>max_sum:
        max_sum=su
        print(max_sum)
    else:
        print(max_sum," in else")
print(max_sum)
