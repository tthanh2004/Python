def is_number(n):
    mylist1 = []
    mylist2 = []
    for i in range(1, n + 1):
        i = input(f"Nhap vao phan tu thu {i}: ")
        try:
            i = float(i)
            mylist1.append(i)
        except ValueError:
            mylist2.append(i)
    
    return mylist1, mylist2

while True:
    n = int(input("N = "))
    if n > 0:
        break

mylist1, mylist2 = is_number(n)

print("Mylist 1 : ")
for n in mylist1:
    print(n, end=' ')
print("\nTBC mylist1 :", sum(mylist1)/len(mylist1))

print("Mylist 2 : ")
for n in mylist2:
    print(n, end='-')
