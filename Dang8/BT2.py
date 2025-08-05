try:
    n = int(input("N = "))
    assert n > 0, "N la so am"
except AssertionError as e:
    while True:
        if n > 0:
            break
        else:
            print(e)
            n = int(input("N = "))

projects = []

for i in range(n):
    manv = set(input(f"Nhap ma nhan vien du an {i+1}: ").split())
    projects.append(manv)

def checkDuAn():
    k = int(input("K = "))
    m = int(input("M = "))
    if 0 <= k < n and 0 <= m < n:
        print(f"Ma nhan vien tham gia du an {k+1} ma khong tham gia du an {m+1}: ", projects[k] - projects[m])
    else:
        print("Du an khong hop le")

def inNhanVienDuAn():
    nhanvien = set.union(*projects)
    print("Ma nhan vien tham gia vao tat ca cac du an: ", nhanvien)
    print("Tong so luong nhan vien : ", len(nhanvien))

def checkTapK():
    k = int(input("K = "))
    if 0 <= k < n:
        tapK = projects[k].copy()
        for i in range(n):
            if i != k:
                tapK -= projects[i]
        print(f"Ma nhan vien da tham gia du an {k+1} ma khong tham gia du an nao khac: ", tapK)
    else:
        print("Du an khong hop le")

def checkDuAnKvaM():
    k = int(input("K = "))
    m = int(input("M = "))
    if 0 <= k < n and 0 <= m < n:
        if projects[k].issubset(projects[m]):
            print(f"Nhan vien tham gia du an {k+1} da tham gia du an {m+1}")
        else:
            print(f"Nhan vien tham gia du an {k+1} chua tham gia du an {m+1}, them vao du an {m+1}")
            projects[m] |= projects[k]
    else:
        print("Du an khong hop le")

checkDuAn()
inNhanVienDuAn()
checkTapK()
checkDuAnKvaM()