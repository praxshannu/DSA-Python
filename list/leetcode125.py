s ="A man, a plan, a canal: Panama"
i=0
j=len(s)-1
        
while i <j:
    if not s[i].isalnum():
        i+=1
    elif not s[j].isalnum():
        j-=1
    else:
        if s[i].lower()!=s[j].lower():
            print( False)
            break
        i+=1
        j-=1
print( True)
