n = int(input("N = "))

def check(n):
    tup = ()
    for i in range(1 ,n + 1):
        i = float(input(f"Nhap so thu {i}: "))
        if i == 0:
            break
        tup += (i,)
    return tup

tup = check(n)

tup = tuple(sorted((x for x in tup if x > 0), reverse=True) +
            sorted(x for x in tup if x < 0))

print(tup)