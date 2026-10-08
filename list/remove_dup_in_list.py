lst =[1]
if 1 in lst :
    print("yes")
lst.extend([6,5,8,7,9,9,8,6,3,2,3,100,9])
lst2=[]
s=set()
for i in range (len(lst)):
    if (i not in s):
        lst2.append(lst[i])
        s.add(i)
print(lst2)
