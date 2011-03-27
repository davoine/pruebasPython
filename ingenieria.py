#!/usr/bin/python
# -*- coding: utf_8 -*-
# ingenieria.py: otro ejemplo de estructuras de datos

def mostrar_avance(tabla_materias, tabla_creditos):
    """Muestra los créditos acumulados por materia

    @param tabla_materias: diccionario con las asignaturas y las materias
    @param tabla_creditos: diccionario con las asignaturas y los créditos
    """

    print "\n Avance en la carrera"
    materias_set = set(tabla_materias.values()))
    materias = []
    # creamos una lista con las materias (para tenerlas ordenadas)
    for mater in materias_set:
        materias.append(mater)
    creditos_por_materia = []
    for mater in tabla_materias.keys():
        
        creditos_por_materia
