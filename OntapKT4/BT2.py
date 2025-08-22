while True:
    xau = input("Xau : ")
    if xau.strip() != "":
        break
    print("-----")

xauNew = xau.split()
sotu = len(xauNew)

maxtu = max(len(tu) for tu in xauNew)
mintu = min(len(tu) for tu in xauNew)

listMax = []
listMin = []
for i in xauNew:
    if len(i) == maxtu:
        listMax.append(i)
    elif len(i) == mintu:
        listMin.append(i)

print("So tu : ",sotu)
print("So tu nho nhat : ",listMin)
print("So tu lon nhat : ",listMax)