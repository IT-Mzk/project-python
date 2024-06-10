print("input name and hight person 1")
name1, hight1= input().split()
print("input name and hight person 2")
name2, hight2= input().split()

hight1= int(hight1)
hight2= int(hight2)

if hight1 > hight2:
    print(name1 + " taller than " + name2)
elif hight1 == hight2:
    print(name1 + " as high as " + name2)
else:
    print(name2 + " taller than " + name1)        
