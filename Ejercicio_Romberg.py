from math import *
def f (x):
    return exp(2-0.5*sin(x))

def trap (f,h,a,b):
    x = []
    y = []
    while (a <= b):
        x.append(a)
        y.append(f(a))
        a = a + h
    n = len(x)
    s = 2*sum (y[1:n-1])
    return h *(y[0]+s+y[n-1])/2

def romberg (N,a,b):
    h = b-a
    i = 0
    t = []
    while i <= N:
        t.append(trap(f,h,a,b))
        i = i + 1
        h = h/2
    print ("P0: ",t)
    t = t[::-1]
    j = 1
    c = 4
    while j <= N:
        i = 0
        while i <= N-j:
            print ("t[i]: ",t[i],"t[i+1]: ",t[i+1])
            t[i] = (c* t[i] - t[i+1])/(c-1)
            i = i + 1
        print ("P"+str(j)+": ", t)
        j = j + 1
        c = c * 4
    
    return t[0]

print (pi*romberg(3,0,2*pi)/2)
        

        
        
