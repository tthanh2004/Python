dayso = input("Day so : ")

daysoNew =[int(x) for x in dayso.split(',')]

A = [i for i in daysoNew if i < 0]
B = [i for i in daysoNew if i >0]

print("So so am :",len(A))
if len(B) > 0:
    print("TBC cac so duong: ",sum(B)/ len(B))