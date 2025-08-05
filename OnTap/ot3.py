def nhap(x):
    tap = set()
    while True:
        phantu = input(f"Nhap vao phan tu cua tap {x}").strip()
        if phantu == '':
            break
        tap.add(phantu)
    return tap

A = nhap("A")
B = nhap("B")

def tapcon():
    if B.issubset(A):
        print("Phan tu thuoc A va B : ", A&B)
    else:
        A.update(B)

def phantuchung():
    if A.isdisjoint(B):
        print("Cac phan tu thuoc A ma khong thuoc B :", A - B)
    else:
        print("Cac phan tu thuoc A hoac B ma khong thuoc ca 2 : ", A ^ B)

def checkX():
    x = input("Nhap x :")
    if x not in A and x not in B:
        A.add(x)
        B.add(x)
    elif x not in A and x in B:
        A.add(x)
    elif x in A and x not in B:
        B.add(x)
    else:
        print("X da co trong A va B")
    return A, B