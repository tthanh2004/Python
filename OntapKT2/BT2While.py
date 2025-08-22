def nhap(x):
    while True:
        try:
            n = int(input(f"Nhap {x}: "))
            if n > 0:
                return n
        except ValueError:
            print("Nhap sai")

A = nhap("A")
B = nhap("B")
C = nhap("C")
n = nhap("n")

k = (n - C) // B
ds = []

x = 0
while A * x <= k:
    y = 0
    max_y = k - A * x
    while y <= max_y:
        ds.append((x, y))
        y += 1
    x += 1

print("Cac cap so:")
for x, y in ds:
    print(f"({x}, {y})")
