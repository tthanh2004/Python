xau = input("Nhap xau: ")
A = tuple(i for i in xau.split() if i.isdigit())
B = set(i for i in xau.split() if i.isalpha())
C = [i for i in xau.split() if i not in A and i not in B]

print(A)
print(B)
print(C)