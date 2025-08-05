xaukytu = input("Nhap xau: ")

def checkXau(xaukytu):
    print(len(xaukytu))
    swapped = xaukytu.swapcase()
    print(swapped)

    loaiso = ' '.join(c for c in xaukytu if not c.isdigit())

    print(loaiso)

    tucandem = input("Nhap tuc an dem: ")
    dem = xaukytu.count(tucandem)

    print(dem)


def checkSoTu(xaukytu):
    for c in xaukytu:
        if xaukytu.count(c) == 1:
            print(c)

def chuanHoa(xaukytu):
    xaukytu = ' '.join(xaukytu.split())

def DemtuNgannhat(xaukytu):
    chuanHoa(xaukytu)
    dstu = xaukytu.split()
    min = min(len(tu) for tu in dstu)
    tungannhat = [tu for tu in dstu if len(tu) == min]
    print("Tu ngan nhat : ", ' '.join(tungannhat))
    print("So luong tu ngan nhat: ", len(tungannhat))
    
checkXau(xaukytu)
checkSoTu(xaukytu)
chuanHoa(xaukytu)
print("Xau da chuan hoa: ", xaukytu)
DemtuNgannhat(xaukytu)