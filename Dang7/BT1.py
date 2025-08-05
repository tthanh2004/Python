def chinhpuong(n):
    return int(n**0.5) * int(n**0.5) == n

def tupleCheckHopLe(n, m):
    a = (n,m)
    return all(x > 0 for x in a)

def tupleCheck(n,m):
    a = ()
    if m > n:
        for i in range(n, m +1):
            if chinhpuong(i):
                a += (i,)

    elif n > m:
        for i in range(m, n + 1):
            if chinhpuong(i):
                a += (i,)

    return a

n = int(input("N = "))
m = int(input("M = "))

if tupleCheckHopLe(n, m):
    print("Hop le")
else:
    print("Khong hop le")

print("Tupble chinh phuong:" , tupleCheck(n, m))