def nhap(x):
    tap = set()
    while True:
        phantu = input(f"Nhap vao phan tu cua tap {x} : ").strip()
        if phantu == '':
            break
        tap.add(phantu)
    return tap

def nhap2():
    try:
        x = int(input("Nhap vao so du an :"))
        assert x > 0 , "X la so am"
    except AssertionError as e:
        while True:
            if x > 0:
                break
            else:
                print(e)
                x = int(input("Nhap vao so du an :"))
    return x