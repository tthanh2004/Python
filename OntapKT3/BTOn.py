def chinhphuong(n):
    if n < 0 :
        return False
    return int(n**0.5)**2 ==n

def nguyento(n):
    if n <= 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
    return True

def fibo(n):
    if n <= 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("N = "))
def nhap(n):
    for i in range(1,n+1):
        i = int(input(f"Nhap vao phan tu thu {i} : "))
        if i == 0:
            break

nhap(n)