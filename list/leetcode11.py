
boo = True
n=14
while boo:
	if n&1==1:
		n>>1=n
	else:
		boo=False
print("the values contigious 1's",boo)
