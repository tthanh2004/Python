def chinhphuong(n):
    return int(n**0.5) * int(n**0.5) == n

def chinhphuongle(n):
    return chinhphuong(n) and n % 2 != 0

def demchinhphuong(n):
    count = 0
    for i in range(1,n+1):
        if chinhphuong(i):
            count += i
    return count


def demchinhphuongle(n, m):
    count = 0
    for i in range(n, m):
        if chinhphuongle(i):
            count += i
    return count

def boi2va3(n, m):
    count = 0
    for i in range(n, m + 1):
        if i % 2 == 0 and i % 3 == 0:
            count += 1
    return count

n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

print(f"Số chính phương trong đoạn [{1}, {n}]: {demchinhphuong(n)}")
print(f"Số chính phương chẵn trong đoạn ({n}, {m}): {demchinhphuongle(n, m)}")
if boi2va3(n, m) == 0:
    print(f"Không có số nào chia hết cho 3 nhưng không chia hết cho 5 trong đoạn [{n}, {m}]")
else:
    print(f"Số chia hết cho 3 nhưng không chia hết cho 5 trong đoạn [{n}, {m}]: {boi2va3(n, m)}")