def convert(d):
    if d >= 8.6:
        r = "A"
    elif d >= 7:
        r = "B"
    elif d >= 5.6:
        r = "C"
    elif d > 4.0:
        r = "D"
    else:
        r = "F"
    return r

d = float(input("Nhap so diem : "))

if d < 0 or d > 10:
    print(d , "Diem khong hop le")
else:
    print("Diem chu" , convert(d))



    