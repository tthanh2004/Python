# Buổi 1 - Bài tập 2
# Viết chương trình nhập vào hai số nguyên n, m và in ra các số nguyên trong khoảng [n, m] chia hết cho 2 và 3.
def chia_cho_2_va_3(n):
    if n < 0:
        return False
    return n % 2 == 0 and n % 3 == 0

def in_chia_cho_2_va_3(n, m):
    if n > m :
        for i in range(n,m+1):
            if chia_cho_2_va_3(i):
                print(i,end=' ')
    elif n < m:
        for i in range(m,n+1):
            if chia_cho_2_va_3(i):
                print(i,end=' ')

n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
in_chia_cho_2_va_3(n, m)