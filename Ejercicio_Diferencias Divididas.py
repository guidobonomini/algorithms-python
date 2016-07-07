def mostrar(t):
    for i in range(0,len(t)):
        for j in range(0,len(t[i])):
            print (t[i][j],end =' ')
        print()
def diferenciasDivididas (x,y,a):
    tabla = [[y[i]] for i in range(0,len(x))]
    for j in range (0,len(x)):
        for i in range (1,len(x)-j):
            z = (tabla[i][j]-tabla[i-1][j])/(x[i+j]-x[i-1])
            tabla [i-1].append(z)
    p = 0
    for k in range(1,len(tabla)):
        s = 1
        for j in range(0,k):
            s = s * (a-x[j])
        p = p + tabla[0][k]*s
    p = p + tabla[0][0]
    
    return p
            
            

x = [0.5,0.6,0.7,0.8,0.9,1]
y = [0.95885,0.94107,0.92031,0.89669,0.87036,0.84147]
a = 1
pol = diferenciasDivididas(x,y,a)
print (pol)

x = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [0.75651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
pol = diferenciasDivididas(x,y,1.3)
print(pol)

x = [1.008, -0.473, -1.936]
y = [0.2, 0.3, 0.4]
pol = diferenciasDivididas(x,y,0)
print(pol)
