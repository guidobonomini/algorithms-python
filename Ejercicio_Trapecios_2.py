def f(x):
    return (x ** 3)/ (1.0 + (x ** 0.5))
    
def trapecios(f, a, b, n):
   h = float(b - a)/n
   x = [a + i * h for i in range(0, n+1)]
   y = [f(z) for z in x]
   return (h/2.0) * (y[0] + 2.0 * sum(y[1:n]) + y [n])

print trapecios (f,1,2,10)

