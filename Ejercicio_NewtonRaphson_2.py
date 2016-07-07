import math

def f(x):
    return x * math.exp(x) - 1.0

def f1(x):
    return math.exp(x) * (1 + x)
			
def newtonraphson(a, f, k, E, f1):
    x = a
    i = 1
    while i <= k and math.fabs(f(x)) > E:
        x = x - (f(x)/f1(x))
        print i,"-",x
        i = i + 1
    return x

print "Inicio"
raiz = newtonraphson(1.0, f, 10, 10**(-4), f1)
