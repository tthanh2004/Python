drl = float(input("Nhap diem ren luyen: "))
gpa = float(input("Nhap diem tich luy: "))

if gpa > 3.6:
    if drl > 90:
        print("Hoc bong Xuat Sac")
    elif drl > 80:
        print("Hoc bong Gioi")
    elif 65 <= drl:
        print("Hoc bong Kha")
    else:
        print("Khong co hoc bong")
elif gpa >= 3.2:
    if drl > 80:
        print("Hoc bong Gioi")
    elif 65 <= drl:
        print("Hoc bong Kha")
    else:
        print("Khong co hoc bong")
elif gpa >= 2.5:
    if 65 <= drl:
        print("Hoc bong Kha")
    else:
        print("Khong co hoc bong")
else:
    print("Khong co hoc bong")