import math
x = float(input("x = "))

fx = 0
if x < 1:
    fx = math.e**x + math.log(x+1)
    print(f"f({x}) = ",fx)
elif x <= 5:
    fx = math.sqrt(x+2) + abs(3-x)**2
    print(f"f({x}) = ",fx)
else:
    fx= (x**2 - 1)/(x*math.sqrt(x-2))
    print(f"f({x}) = ",round(fx,2))

