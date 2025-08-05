def chinhphuong(n):
    return int(n**0.5) * int(n**0.5) == n

def chinhphuong_chan(n):
    return chinhphuong(n) and n % 2 == 0

def dem_chinhphuong(n):
    count = 0
    for i in range(1,n+1):
        if chinhphuong(i):
            count += 1
    return count


def dem_chinhphuong_chan(n, m):
    count = 0
    for i in range(n, m):
        if chinhphuong_chan(i):
            count += 1
    return count

def dem_chia_het_3_khong_chia_het_5(n, m):
    count = 0
    for i in range(n, m + 1):
        if i % 3 == 0 and i % 5 != 0:
            count += 1
    return count

n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

print(f"Số chính phương trong đoạn [{1}, {n}]: {dem_chinhphuong(n)}")
print(f"Số chính phương chẵn trong đoạn ({n}, {m}): {dem_chinhphuong_chan(n, m)}")
if dem_chia_het_3_khong_chia_het_5(n, m) == 0:
    print(f"Không có số nào chia hết cho 3 nhưng không chia hết cho 5 trong đoạn [{n}, {m}]")
else:
    print(f"Số chia hết cho 3 nhưng không chia hết cho 5 trong đoạn [{n}, {m}]: {dem_chia_het_3_khong_chia_het_5(n, m)}")