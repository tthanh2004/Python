def tong1(n):
    sum = 0
    for i in range(1,n +1):
        sum += 1/(2 * i)
    return sum

def tong2(n):
    tichdayso = 1
    sum = 1
    for i in range(2, n + 1):
        tichdayso *= i
        sum += (-1)**(i-1)*tichdayso(i)
    return sum

def tong3(n):
    tichdayso = 1
    sum = 0
    for i in range(1, n + 1):
        tichdayso *= i
        sum += i/tichdayso
    return sum

def tong4(n):
    tongdayso = 0
    sum = 0
    for i in range(1, n + 1):
        tongdayso += i
        sum += i / tongdayso
    return sum

def tong5(n,x):
    tichdayso = 1
    sum = 1
    for i in range(1, n + 1):
        ketqua *= 2*i
        sum += ((-1)**i) * (x**(2*i))/(tichdayso)
    return sum


n = int(input("Nhap n : "))
x = int(input("Nhap x : "))

print(f"Tong 1:", tong1(n))
print(f"Tong 5:", tong5(n, x))