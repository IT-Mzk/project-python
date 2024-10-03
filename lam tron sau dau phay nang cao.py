giaTriA = input() #Nhap gia tri dau tien tu ban phim
giaTriB = input() #Nhap gia tri thu hai tu ban phim
isPhraseDone= False

try: #Khoi lenh co the phat sinh loi
    soA = float(giaTriA) #Ep kieu giaTriA sang kieu so thuc
    soB = int(giaTriB) #Ep kieu giaTriB sang kieu so nguyen
    isPhraseDone= True

except: #Khoi lenh duoc thuc thi khi loi xay ra
    print("Dinh dang dau vao khong hop le!") #In thong bao

if isPhraseDone:    
     print('{0:.{1}f}'.format(soA, soB))