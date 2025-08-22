def nhapxau(hangso):
    while True:
        xau = input(f"Xau {hangso} = ")
        if xau != "":
            break
    return xau

A = nhapxau("A")

# tách xâu
xauMoi = A.split()

# ab abc abd => {'ab' , 'abc' , 'abd'} --> split('')
# 1,2,3,4,5,6 --> split(',')
# Đếm số phần tử

print(len(xauMoi)) # 3
mintu = min(len(x) for x in xauMoi) # 2

#in ra thằng đầu tiên:
listTu = []
for i in xauMoi:
    if len(i) == mintu:
        listTu.append(i)
# ab ac ad abd
print(listTu[0])
