xau = input("Xau : ")

xauNew = xau.split()

# Từ dài nhất cuối cùng
maxTu = max(len(tu) for tu in xauNew)

listTu = [tu for tu in xauNew if len(tu) == maxTu]

tuFinal = listTu[::-1]

print(tuFinal[0])

# Chuẩn hóa
xauChuanHoa = ' '.join(tu for tu in xauNew)
xauChuanHoa = xauChuanHoa.title()
print("Xau chuan hoa:", xauChuanHoa)


#Xóa ký tự , số

xauXoa = ''.join(c for c in xau if c.isalpha() or c.isspace())
print("Xau Xoa : ",xauXoa)