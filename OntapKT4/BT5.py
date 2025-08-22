chuoiso = input("Chuoi so : ")

chuoisoNew = chuoiso.split(",")

dayso = [float(i) for i in chuoisoNew if float(i) < 0]

TBC = sum(dayso)/len(dayso)

print("TBC : ",TBC)