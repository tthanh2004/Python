def chinhphuong(n):
    return int(n**0.5) * int(n**0.5) == n

def chinhphuongchan(n):
    return chinhphuong(n) and n % 2 == 0

def is_number(n):
    mylist1 = []
    mylist2 = []
    mylist3 = []
    mylist4 = []
    for i in range(1, n + 1):
        if i % a == 0 and i % b == 0:
            mylist1.append(i)
        elif i % 3 == 0 and i % 4 != 0:
            mylist2.append(i)
        elif chinhphuongchan(i):
            mylist3.append(i)
        else:
            mylist4.append(i)
    return mylist1, mylist2, mylist3, mylist4

n = int(input("N : "))
a = int(input("A : "))
b = int(input("B : "))

mylist1, mylist2, mylist3, mylist4 = is_number(n)

print("Mylist1 :")
for n in mylist1:
    print(n, end=' ')

print("\nMylist2 :")
for n in mylist2:
    print(n, end=' ')

print("\nMylist3 :")
for n in mylist3:
    print(n, end=' ')

print("\nMylist4 :")
for n in mylist4:
    print(n, end=' ')