def nhapDS(tenDL):
    ds = set()
    while True:
        mnv = input(f"Nhap ma nhan vien {tenDL} (Enter de dung): ")
        if mnv.strip() == "":
            break
        ds.add(mnv)
    return ds

dl1 = nhapDS("Dai ly 1")
dl2 = nhapDS("Dai ly 2")

chi_dl1 = tuple(dl1 - dl2)
print("Nhan vien chi o dai ly 1:", chi_dl1)

ca2 = dl1 & dl2
print("So nhan vien tham gia ca 2 dai ly:", len(ca2))

khong_ca2 = dl1 ^ dl2
print("Nhan vien khong tham gia dong thoi 2 dai ly:", khong_ca2)
