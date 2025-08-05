def nhap(x):
    tap = set()
    while True:
        phan_tu = input(f"Nhap phan tu cua tap {x} (nhan Enter de dung): ").strip()
        if phan_tu == '':
            break
        tap.add(phan_tu)
    return tap

A = nhap("A")
B = nhap("B")

def checkTapCon(A , B):
    if B.issubset(A):
        print("Phan tu thuoc ca A va B : ", A & B)
    else:
        A.update(B)
    return A

def checkPTChung(A , B):
    if A.isdisjoint(B):
        print("Cac phan tu thuoc A ma khong thuoc B : ", A - B)
    else:
        print("Cac phan tu thuoc A hoac B ma khong thuoc ca 2: ", A ^ B)

def checkX(A , B):
    x = input("Nhap x: ")
    if x not in A and x not in B:
        A.add(x)
        B.add(x)
    elif x not in A and x in B:
        A.add(x)
    elif x in A and x not in B:
        B.add(x)
    else:
        print("X da co trong A va B")
    return A , B


A = checkTapCon(A, B)
print("A sau khi them tap con: ", A)

checkPTChung(A, B)

A, B = checkX(A, B)
print("A sau khi them x: ", A)
print("B sau khi them x: ", B)
