def f(x):
    return (x ** 3)/ (1.0 + (x ** 0.5))
    
def trapecios(f,a, b):
   return  ((b - a)/2.0) * (f(a) + f(b))

print trapecios (f,1,2)

