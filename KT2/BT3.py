xau1 = input("Nhap xau 1: ")
xau2 = input("Nhap xau 2: ")

def chuanhoa(xau):
    xau = ' '.join(xau.split())
    return ' '.join(word.title() for word in xau.split())

def khacnhau(xau1, xau2):
    set1 = set(xau1.split())
    set2 = set(xau2.split())
    return set1 - set2 | set2 - set1

if xau1 in xau2 or xau2 in xau1:
    xau1 = chuanhoa(xau1)
    xau2 = chuanhoa(xau2)
    print("Xau 1 sau chuan hoa:", xau1)
    print("Xau 2 sau chuan hoa:", xau2)
else:
    print("Cac thanh phan khac nhau giua hai xau:", khacnhau(xau1, xau2))

k = int(input("Nhap vao so k: "))
xau = xau1.split() + xau2.split()
words = [word for word in xau if len(word) > k]
print(f"Cac tu co do dai > {k}:", words)