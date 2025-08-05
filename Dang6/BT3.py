def fibo(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)
    
n = int(input("N = "))

mylist = [fibo(i) for i in range(1, n + 1) if fibo(i) <= n]

print("Danh sach : ",mylist)