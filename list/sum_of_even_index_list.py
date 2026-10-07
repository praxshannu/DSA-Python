a=[4,5,5,2,3,2,12,8,7,9]
ls=0
#for i in range(len(a)):
#    if i%2==0:
for i in range(0,len(a),2):
    ls+=a[i]
print(ls)
