# Hàm
chuoi = input("Chuoi = ")

# isdigit -> số từ 0-9
# isalpha -> chữ
# isnumeric -> số

# Chuẩn hóa
xauChuanHoa = ' '.join(tu for tu in xauNew)
xauChuanHoa = xauChuanHoa.title()
print("Xau chuan hoa:", xauChuanHoa)


#Xóa ký tự , số

xauXoa = ' '.join(c for c in xau if c.isalpha() or c.isspace())
print("Xau Xoa : ",xauXoa)