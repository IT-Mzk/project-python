print("input 3 numbers:")
a, b, c= map(float, input().split())
if a+b>c and a+c>b and b+c>a:
    print("{}, {}, {} are the three sides of a triangle".format(a,b,c))    
else:
    print("{}, {}, {} are not the three sides of a triangle".format(a,b,c))   
