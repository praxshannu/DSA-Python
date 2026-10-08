lst=[6,5,8,3,4,2,2,34,6]
lst.extend([6,5,8,7,9,9,8,6,3,2,3,100,9])
s={}
for i in lst:
    if (i not in s):
        s[i]=1
    else:
        s[i]=s[i]+1
for i in s:
    print(i,"-",s[i])

