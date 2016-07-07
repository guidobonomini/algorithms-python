import math

def f(x):
    return (math.e/3.0) * x* math.exp(-x/3.0) - 0.25
			
def f1(x):
    return (math.e/3.0) *math.exp(-x/3.0) * (1-(x/3.0))
			
def newtonraphson(a, f, k, E, f1):
    x = a
    i = 1
    while i <= k and math.fabs(f(x)) > E:
        x = x - (f(x)/f1(x))
        print i,"-",x
        i = i + 1
    return x

print "Inicio"
raiz = newtonraphson(4.0, f, 10, 10**(-4), f1)
