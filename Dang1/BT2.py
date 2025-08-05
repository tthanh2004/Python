def diemtichluy(diem):
    if diem >= 3.6 :
        r = "Xuat sac"
    elif diem >= 3.2:
        r = "Gioi"
    elif diem >= 2.5:
        r = "Kha"
    elif diem >= 2.0:
        r = "Trung binh"
    else:
        r = "Yeu"
    return r

try:
    diem = float(input("Nhap diem tich luy: "))
    assert diem >= 0 and diem <= 4, "Diem khong hop le"
    print("Xep loai:", diemtichluy(diem))
except AssertionError as e:
    print(e)

except ValueError:
    print("Diem phai la so")