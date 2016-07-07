import math

def f(x):
    return x * math.exp(x) - 1.0
						
def biseccion(a, b, eps, f, k):
    i = 0
    x = float(a + b)/2.0
    while i <= k and math.fabs(f(x)) > eps:
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        i = i + 1
        x = float(a + b)/2.0
    return x

print "Inicio"
raiz = biseccion(0, 1, 10**(-4), f, 7)
print raiz
