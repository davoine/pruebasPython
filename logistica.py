from numpy import *

def logistica(x0,n):
    try:
        verdadero = (x0 > 0) or (x0<1)
    except ValueError:
        print "Error, x0 debe estar entre 0 y 1"
        
    x = x0
    aes = range(0,1,0.1)
    for k in aes:
        a = aes[k]
        y = numpy.zeros([len(a),n])
        for i in range(2000):
            x = a*x*(1-x)
        for i in range(n):
            y[i][k]=a*x*(1-x)
