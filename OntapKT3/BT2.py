xau = input("Nhap ds: ")

def nguyento(n):
    n = int(n)
    if n <= 1 :
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True

def chinhphuong(n):
    n = int(n)
    if n < 0 :
        return False
    return int(n**0.5) ** 2 == n


def checkSo(xau):
    listInt = [int(i) for i in xau.split()]
    A = tuple(i for i in listInt if nguyento(i))
    B = set(i for i in listInt if chinhphuong(i))

    listSX = sorted((i for i in listInt if i > 0), reverse=True) + sorted(i for i in listInt if i < 0)
    return A , B , listSX

A , B , listSX = checkSo(xau)

print("Nguyen to: ",A)
print("Chinh phuong: ",B)
print("Sap xep:",end=' ')
for i in listSX:
    print(i,end=' ')