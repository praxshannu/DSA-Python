time = int(input())
print((time//3600) , "H")
time =time % 3600
print((time //60) , "M")
time = time% 60 
print(time , "S")

