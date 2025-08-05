def chinhphuong(n):
    return int(n**0.5) * int(n**0.5) == n

def chinhphuongchan(n):
    return chinhphuong(n) and n % 2 == 0

n = int(input("N : "))
a = int(input("A : "))
b = int(input("B : "))

mylist1 = [i for i in range(1, n + 1) if i % a == 0 and i % b == 0]
mylist2 = [i for i in range(1, n + 1) if i % 3 == 0 and i % 4 != 0]
mylist3 = [i for i in range(1, n + 1) if chinhphuongchan(i)]

print("Mylist1:")
print(mylist1)

print("Mylist2:")
print(mylist2)

print("Mylist3:")
print(mylist3)