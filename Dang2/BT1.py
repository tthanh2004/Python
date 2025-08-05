def chinhphuong(n):
    return int(n**0.5) * int(n**0.5) == n

def in_chinhphuong(n,m):
    for i in range(n,m+1):
        if chinhphuong(i):
            print(i, end=' ')

n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

in_chinhphuong(n, m)