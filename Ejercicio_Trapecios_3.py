def f(x):
    return (x ** 3)/ (1.0 + (x ** 0.5))
    
def trapecios(f, a, b, n):
   h = float(b - a)/n
   x = [a + i * h for i in range(0, n+1)]
   y = [f(z) for z in x]
   I = sum(y[1:n:2])
   p = sum(y[2:n:2])
   return (h/3.0) * (y[0] + 4* I + 2 * p + y [n])

print trapecios (f,1,2,10)

