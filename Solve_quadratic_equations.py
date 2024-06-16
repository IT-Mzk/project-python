#giai phuong trinh bac hai ax^2+bx+c=0
a= float(input("nhap so a"))
b= float(input("nhap so b"))
c= float(input("nhap so c"))
delta= b*b-4*a*c
if delta<0 : print("phuong trinh vo nghiem")
elif delta==0 : print("phuong trinh co nghiem kep x1=x2=",-b/(2*a))
else:
    print("phuong trinh co 2 nghiem phan biet")
    import math
    x1= (-b-math.sqrt(delta))/(2*a)
    x2= -b/a-x1
    print("x1=",x1,"x2=",x2)
    
