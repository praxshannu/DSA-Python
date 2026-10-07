n = 5
ch=97
for i in range(n):
    for j in range(n-i):
        print("_",end="")
        
    for j in range(2*i+1):

        if(j<(2*i+1)/2):
            print(chr(ch+j),end="")
        else:
            print(chr(ch+(2*i+1)-j-1),end="")
    for j in range(n-i):
         print("_",end="")
        
    print()
