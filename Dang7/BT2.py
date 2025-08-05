n = int(input("N = "))

def check(n):
    a = ()
    for i in range(1 ,n + 1):
        i = int(input(f"Nhap so thu {i} : "))
        if i == 0:
            break
        a += (i,)
    return a


tupleCheck = check(n)

if len(tupleCheck) == 0:
    print("Day rong")
else:
    if all(x > 0 for x in tupleCheck):
        print("TBC : ", sum(tupleCheck)/len(tupleCheck))
    elif all(x < 0 for x in tupleCheck):
        print("Tong : ", sum(tupleCheck))
    else:
        soduong = tuple(x for x in tupleCheck if x > 0)
        print("Cac so duong : ", soduong)
