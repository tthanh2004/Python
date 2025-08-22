def nhapDiem(i):
    diem = int(input(f"Diem {i}: "))
    if diem < 0 or diem > 10:
        while True:
            diem = int(input(f"Diem {i}: "))
            if diem >= 0 and diem <= 10:
                break
    return diem

def printTable(sv_dict, title="Danh sach sinh vien"):
    print("| Ma SV  | Diem |")
    for msv, diem in sv_dict.items():
        print(f"| {msv:<6} | {diem:<4} |")
    print("+--------+------+")


def createDict():
    i = 1
    sv_dict = {}
    while True:
        msv = input(f"Ma {i}: ")
        if msv == '':
            break
        diem = nhapDiem(i)
        i += 1
        sv_dict[msv] = diem

    return sv_dict

def delSV(sv_dict):
    msv = input("Nhap ma sinh vien can xoa: ")
    if msv in sv_dict:
        del sv_dict[msv]
    else:
        diemNew = nhapDiem()
        sv_dict[msv] = diemNew
    return sv_dict

def maxDiem(sv_dict):
    listSV = []
    maxDiem = max(sv_dict.values())
    for msv , diem in sv_dict.items():
        if diem == maxDiem:
            listSV.append((msv,diem))
    return listSV

def capnhatDiem(sv_dict):
    msvSearch = input("Nhap vao ma sinh vien can tim kiem : ")
    if msvSearch in sv_dict:
        diemNew = nhapDiem()
        sv_dict[msvSearch] = diemNew
    else:
        print("Khong tim thay ma sinh vien")
    return sv_dict

def thiLai(sv_dict):
    svThiLai = {}
    for msv, diem in sv_dict.items():
        if diem < 5:
            svThiLai[msv] = diem
    return svThiLai

sv_dict = createDict()
printTable(sv_dict, "Danh sach ban dau")


sv_dict = delSV(sv_dict)
print(sv_dict)

print("Sinh vien diem cao nhat:", maxDiem(sv_dict))

sv_dict = capnhatDiem(sv_dict)
print(sv_dict)

print("Sinh vien thi lai:", thiLai(sv_dict))

