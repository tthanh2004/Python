def chinhphuong(n):
    return int(n**0.5)**2 == n

def nhap():
    A = []
    B = ()
    C = set()
    n = int(input("Nhap vao N = "))
    a = []
    for i in range(1 , n+1):
        i = (input(f"Nhap vao phan tu {i} : "))
        try:
            x = int(i)
            A.append(x)
        except ValueError:
            try:
                x = float(i)
                B += (x,)
            except ValueError:
                C.add(i)
    return A, B, C

A, B, C = nhap()

count = sum(chinhphuong(i) for i in A)
print("So luong so chinh phuong trong A:", count)

if B:
    newlistB = [i for i in B if i < max(B)]
    print("Cac so nho hon so lon nhat trong B:", newlistB)
else:
    print("Khong co so nao trong B")

if C:
    c = max(len(s) for s in C)
    newlistC = [s for s in C if len(s) == c]
    print("Cac chuoi co do dai lon nhat trong C:", newlistC)