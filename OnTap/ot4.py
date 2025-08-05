A = int(input("Nhap so A: "))
B = int(input("Nhap so B: "))
C = int(input("Nhap so C: "))
n = int(input("Nhap so N: "))

list = []

for i in range(1,int((n - C)/A)):
    for j in range(1, int((n - C - A*i) / A*B)):
        if A * i + A * B * j + C < n :
            list.append((i, j))

for c in list:
    print(c)