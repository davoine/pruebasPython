#!/usr/bin/env python
# -*- coding: utf-8 -*-
# primos.py: calcula la descomposición en factores primos

def primos():
    """Calcula la descomposición en factores primos del número a"""

    sa = raw_input("Ingrese un número natural:")

    try:
        a = int(sa)
    except ValueError:
        print "Error,", sa, "no es un número natural"
        raw_input("Ingrese un número natural:")
        a = int(sa)
    
    #construyamos una lista de los números primos hasta a
    factoresprimos = []
    for k in range(1,a+1):
        bandera = True
        for i in range(3,k):
            if k%i == 0:
                bandera = False
        if bandera == True:
            factoresprimos.append(k)
    print factoresprimos
