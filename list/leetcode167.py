numbers=[2,4,6,7,8,10,13,16,18,20]
l = 0
res=[]
r= len(numbers) - 1
target = 21
while l < r:
    if numbers[l]+numbers[r] == target:
        res.extend([l+1,r+1])
        break
    elif numbers[l]+numbers[r]>target:
        r-=1
    elif numbers[l]+numbers[r]<target:
        l+=1
    else:
        pass
print(res)
