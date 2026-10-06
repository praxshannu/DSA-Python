year = 2000
if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("it's a leap year")
        else: 
            print("not a leap year")
    else:
        print(" leap year")
else:
    print("not a leap year")

