with open('input.inp', 'r') as fileinp:
    ten = fileinp.readline().rstrip('\n')

    # Đọc dòng tiếp theo và bỏ qua nếu là dòng trống
    tuoihientai_str = fileinp.readline().strip()  # .strip() bỏ khoảng trắng hai bên, kể cả dòng trống
    
    if tuoihientai_str.isdigit():  # Kiểm tra nếu dòng không trống và là số nguyên
        tuoihientai = int(tuoihientai_str)
    else:
        raise ValueError('Giá trị tuổi không hợp lệ hoặc dòng trống.')

with open('output.out', 'w') as fileout:
    fileout.write('Năm sau tuổi của {} sẽ là {}'.format(ten, tuoihientai + 1))
