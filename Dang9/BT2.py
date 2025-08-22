s = input("Nhap xau : ")

s = s.replace(" ","").lower()

if s == s[::-1]:
    print("True")

