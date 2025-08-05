def chinhphuong(n):
    return n == int(n**0.5) ** 2

def nguyento(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

def hoanhao(n):
    if n < 2 :
        return False
    tong = sum(i for i in range(1,n) if n % i == 0)
    return tong == n

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def trifibo(n):
    a,b,c = 0,1,1
    while a < n :
        a,b,c = b,c,a+b+c
    return a == n
