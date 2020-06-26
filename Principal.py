#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:18:16 2020

@author: lbeltran
"""


from Grafo import Grafo
import re

G = Grafo("Grafo")
archivo = open("Topologico.txt")
lineas = archivo.readlines()
for linea in lineas:
    a = re.findall("\S+", linea)
    if ( len(a)>2 ):
        G.addNodo(a[0])
        G.addNodo(a[1])
        G.getNodo(a[0]).addAdyacente(G.getNodo(a[1]))
        G.addArco(a[0],a[1],float(a[2]))
archivo.close()
"""
G.BFS(G.getNodo("s"))
#G.show()
archivo.close()
archivo = open("salida.txt","w")
archivo.write("{:^5}".format(""))
for nodo in G.V.values():
    a = nodo.nombre
    archivo.write("{:^5}".format(a))
  

for b in G.V.values():
    G.BFS(b)
    archivo.write("\n")  
    archivo.write("{:^5}".format(b.nombre))
    for nodo in G.V.values():
        a = nodo.d
        archivo.write("{:^5}".format(a))
"""



lista=G.ordenamientoTopologico()
print(lista)







