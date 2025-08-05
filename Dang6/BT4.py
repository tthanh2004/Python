n = int(input("N = "))
a = int(input("A = "))
b = int(input("B = "))


def f(x,y):
    return a * x + b * y

list = []
count = 0
for i in range(1, (n//a)):
    for j in range(1, (n-a*i//b)):
        if f(i,j) < n :
            list.append((i, j))
            count += 1

print("So nghiem : ", count)
print("Danh sach : ", list)