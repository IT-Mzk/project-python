giatri=input("input number decimal:")
flag= False
try:
    sothapphan=int(giatri)
    flag= True
except:
    print("ko hop le")
if flag:
    print("so thap phan %d trong bat phan la %o"% (sothapphan, sothapphan))        
