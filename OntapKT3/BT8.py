def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("N = "))
ds_dict = {i: fibonacci(i) for i in range(1, n + 1)}

def printTable(ds_dict):
    print("Key     |   Values")
    for key,values in ds_dict.items():
        print(f"{key:<10}|{values:<5}")

printTable(ds_dict)