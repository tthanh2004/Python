def chinhphuong(n):
    return int(n**0.5) ** 2 == n

def tupChuoi():
    chuoi = input("Nhap vao chuoi : ")

    ds = chuoi.split(',')

    tupCP = ()
    tupNon = ()

    for item in ds:
        x = int(item.strip())
        if chinhphuong(x):
            tupCP += (x, )
        else :
            tupNon += (x, )
    return tupCP , tupNon

tupCP , tupNon = tupChuoi()

print(tupCP)
print(tupNon)
