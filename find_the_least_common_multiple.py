#tim boi chung nho nhat
def UCLN(a,b):
    while a!=b:
        if a>b: a=a-b
        else: b=b-a
    return a

a= int(input("input number a:"))
b= int(input("input number b:"))
print("BCNN cua",a,"va",b,"la:",int(a*b/UCLN(a,b)))
