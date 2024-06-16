#tong cua cac giai thua
def giaithua(n):
    if n==0: return 1
    gt = 1
    for i in range(1,n+1):
        gt = gt*i
    return gt    

n= int(input("nhap so nhuyen duong n"))
s=0
for i in range(1,n+1):
    s=s+giaithua(i)
print("tong se la:",s)    
