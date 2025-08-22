#  nhập vào n tìm ước chung của a và b trong đoạn n m
def fibo(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
# Tính toán
# math.log(x,10)
# math.log(x , math.e)
# exp(x) -> e mũ x
print(round(x,10)) # --> in ra sau dấu phẩy 10 chữ số
def nhap(hangso):
    while True:
        y = int(input(f"{hangso} = "))
        if y > 0:
            break
    return y

# LIST

## genderate

# chia het cho 3 tu 1 den n
n = nhap("N")

list3 = [i for i in range (1,n+1) if i % 3 == 0]

list3.append(1)
print(list3)

# SET , TUPLE

A = tuple(fibo(i) for i in range (1,n+1))
A += (3,)
print(A)

B = set(i for i in range (1,n+1) if fibo(i))
B.add(25)
print(B)

## SET

# Tập con
# -- Check tập con issubset B là con A trong ngoặc : cha, ngoài : con
B.issubset(A)
# -- Thêm A vào B
A.update(B)

# -- Kiểm tra phần tử chung
A.isdisjoint(B)

# -- Phần tử chung của A và B:
print(A & B)

# -- Thuộc A mà không thuộc B :
print(A - B)

# -- Phần tử thuộc cả A và B
print(A | B)

# -- Thuộc A hoặc B nhưng không phải cả 2 : không phải phần tử chung
print(A ^ B)

sum , len , sorted , min , max : chung