def hello(tuoi,gioitinh):
    if gioitinh == "nam":
        if tuoi <= 20:
            r = "Chao em"
        elif tuoi <= 40:
            r = "Chao anh"
        elif tuoi < 60:
            r = "Chao bac"
        else:
            r = "Chao ong"
    elif gioitinh == "nu":
        if tuoi <= 20:
            r = "Chao chi"
        elif tuoi <= 40:
            r = "Chao co"
        elif tuoi < 60:
            r = "Chao bac"
        else:
            r = "Chao ba"
    return r

try:
    hoten = str(input("Nhap ho ten : "))
    gioitinh = str(input("Nhap gioi tinh : "))
    tuoi = int(input("Nhap tuoi : "))
    print("Xin chao", hoten, ":", hello(tuoi, gioitinh))
    assert tuoi >= 0, "Tuoi khong hop le"
except AssertionError as e:
    print(e)
except ValueError:
    print("Tuoi phai la so")