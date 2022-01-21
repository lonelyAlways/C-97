intro=input("Ab bol bolna mc")
print(intro)
ccount=0
wcount=1
for i in intro: 
    ccount+=1
    if(i==" "):
        wcount+=1
print("The number of characters are : ")
print(ccount)
print("The number of words are : ")
print(wcount)