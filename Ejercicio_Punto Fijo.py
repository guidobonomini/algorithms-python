import math

def g(x):
    return x - x ** 3 + 4 * (x ** 2) - 10

def g1(x):
    return math.sqrt(math.abs((10/x) - x ** 3))

def g2(x):
    return 1/2 * math.sqrt(math.abs(10 - x ** 3))

def g3(x):
    return math.sqrt(math.abs(10/(4 + x)))

def g4(x):
    return x - ((x ** 3) + 4 * (x ** 2) - 10)/3 * x ** 2 + 8 * x

def puntofijo(g, k, eps, x):
    i = 1
    x1 = x2 = x3 = x4 = x5 = x
    while i <= k and math.fabs(g(x)) > eps:
        #x1 = g(x)
        x2 = g1(x)
        x3 = g2(x)
        x4 = g3(x)
        x5 = g4(x)
        print i, ":",("%.4f"%x2)," - ",("%.4f"%x3)," - ",("%.4f"%x4)," - ",("%.4f"x5)
        i = i + 1
    return (x1, x2, x3, x4, x5)

r1, r2, r3, r4, r5 = puntofijo()

        
