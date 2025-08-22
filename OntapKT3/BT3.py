A = ()
xau = input("Xau : ")

xauNew = xau.split()

min_xau = min(len(i) for i in xauNew)

for i in xauNew:
    if len(i) == min_xau:
        A += (i, )

print("So tu ngan nhat: ",min_xau)
print("Cac tu khac :",A)