def chinhphuong(n):
    return int(n**0.5)**2 == n

def nhap(x):
    while True:
        y = int(input(f"{x} = "))
        if y > 0:
            return y

n = nhap("N")
m = nhap("M")

def tupleSX(n):
    listSo = []

    for i in range(1,n+1):
        i = float(input(f"Nhap so thu {i} = "))
        listSo.append(i)

    tuple1 = sorted((i for i in listSo if chinhphuong(i)),reverse=True)
    tuple2 = sorted(i for i in listSo if i not in tuple1)
    tupleSX = tuple1 + tuple2
    return tupleSX

def ListChia5(n,m):
    listNew = []
    if n > m:
        for i in range(m, n+1):
            if i % 5 == 0:
                listNew.append(i)
    else:
        for i in range(n, m+1):
            if i % 5 == 0:
                listNew.append(i)
    return listNew

tupleKQ = tupleSX(n)
print("Tuple: ",tupleKQ)
ListKQ = ListChia5(n,m)
print("List chia het cho 5 : ",ListKQ)