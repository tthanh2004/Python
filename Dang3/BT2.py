def fibo(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)
    
def dem_fibonacci(n, m):
    d = 0
    for i in range(n, m + 1):
        if fibo(i) <= m:
            d += 1
    return d

n = int(input("n: "))
m = int(input("m: "))

print(f"So fibonacci trong doan [{n} , {m}] : {dem_fibonacci(n, m)}")