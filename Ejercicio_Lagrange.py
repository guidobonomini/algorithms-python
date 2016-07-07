import math

def polLagrange(x, y, a):
    n = len(x)
    s = 0

    for i in range(0,n):
        p = 1
        for k in range (0, n):
            if(k != i):
                p = p * float(a - x[k]) / (x[i] - x[k])
        s = s + p * y[i]
    return s

x_aux = [i for i in range (1,7) if i != 5]
y_aux = [math.exp(i) for i in x_aux]
resultado = polLagrange(x_aux, y_aux, 5)
print resultado
