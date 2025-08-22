n = int(input("N = "))

def nhap():
    NewDict = {}
    for i in range(1, n+1):
        maSP = input(f"Ma san pham {i} : ")
        soLuong = int(input(f"So luong {i} : "))
        NewDict[maSP] = soLuong
    return NewDict
    
def checkSP(NewDict):
    maSearch = input("Nhap vao ma san pham can tim : ")
    if maSearch in NewDict:
        del NewDict[maSearch]
    else:
        soluong = int(input("Nhap so luong them moi : "))
        NewDict[maSearch] = soluong
    return NewDict

def MinSL(NewDict):
    setMin = set()
    minSoluong = min(NewDict.values())
    for msp , sl in NewDict.items():
        if sl == minSoluong:
            setMin.add((msp,sl))
    return setMin

DictNew = nhap()
print("Tu dien : ",DictNew)

checkSP(DictNew)
print("Tu dien moi : ",DictNew)

setNew = MinSL(DictNew)
print("Set : ",setNew)