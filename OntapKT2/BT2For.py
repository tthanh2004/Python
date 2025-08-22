def nhap(x):
    while True:
        n = int(input(f"{x}: "))
        if n > 0:
            return n


n = nhap("N")
A = nhap("A")
B = nhap("B")
C = nhap("C")

ds = []
k = n - C
max_i = int((k / B) / A)

for i in range(1, max_i + 1):
        max_j = int((k / B ) - A * i)
        if max_j >= 1:
            for j in range(1,max_j + 1):
                ds.append((i,j))

print("Cac cap so: ")
for i in ds:
    print(i)