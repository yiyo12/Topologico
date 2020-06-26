#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:33:16 2020

@author: lbeltran
"""

from Nodo import Nodo
from Arco import Arco

class Grafo:
    def __init__(self,nombre):
        self.nombre=nombre
        self.V = {}
        self.E = []
        self.tiempo = 0
        
    def addNodo(self, nodo):
        if nodo not in self.V:
            self.V[nodo]= Nodo(nodo)
            
    def getNodo(self, nodo):
        if nodo not in self.V:
            return None
        return self.V[nodo]
    
    def addArco(self, origen, destino, costo):
        self.E.append(Arco(origen,destino,float(costo)))
        
    def show(self):
        for i in self.V.values():
            i.show()
            
    def BFS(self, s):
        for nodo in self.V.values():
            nodo.d= float('inf')
            nodo.color = "Blanco"
            nodo.padre = None
        s.color= "Gris"
        s.d = 0
        Q = []
        Q.append(s)
        while (len(Q)>0):
            u = Q.pop(0)
            for v in u.adjunta:
                if v.color == "Blanco":
                    v.color= "Gris"
                    v.d = u.d + 1
                    v.padre = u
                    Q.append(v)
            u.color= "Negro"
        
    def DFS(self):
        for u in self.V.values():
            u.color = "Blanco"
            u.padre = None
        self.tiempo = 0
        for u in self.V.values():
            if u.color == "Blanco":
                self.DFS_Visit(u)
                
    def DFS_Visit(self, u):
        u.color = "Gris"
        self.tiempo = self.tiempo + 1
        u.d = self.tiempo
        for v in u.adjunta:
            if v.color == "Blanco":
                v.padre = u
                self.DFS_Visit(v)
        u.color= "Negro"
        self.tiempo = self.tiempo + 1
        u.f = self.tiempo
        
    def SCC_Visit(self, u, lista):
        u.color = "Gris"
        self.tiempo = self.tiempo + 1
        u.d = self.tiempo
        lista.append(u.nombre)
        for v in u.adjunta:
            if v.color == "Blanco":
                v.padre = u
                self.SCC_Visit(v,lista)
        u.color= "Negro"
        self.tiempo = self.tiempo + 1
        u.f = self.tiempo
        
    def getTranspuesta(self):
        G = Grafo("T")
        for a in self.E:
            G.addNodo(a.destino)
            G.addNodo(a.origen)
            G.getNodo(a.destino).addAdyacente(G.getNodo(a.origen))
            G.addArco(a.destino,a.origen,a.costo)
        return G
    
    def SCC(self):
        self.DFS()
        G= self.getTranspuesta()
        V= sorted(self.V.values(), key= lambda n:n.f,reverse=True)        
        for u in G.V.values():
            u.color = "Blanco"
            u.padre = None
        self.tiempo = 0
        U=[]
        for a in V:
            U.append(a.nombre)
        lista=[]
        for a in U:            
            u=G.getNodo(a)
            if u.color == "Blanco":
                lista2=[]
                lista.append(lista2)
                G.SCC_Visit(u,lista2)
        return lista
        
        
    def ordenamientoTopologico(self):
           self.DFS()
        G= self.getTranspuesta()
        V= sorted(self.V.values(), key= lambda n:n.f,reverse=True)        
        for u in G.V.values():
            u.color = "Blanco"
            u.padre = None
        self.tiempo = 0
        U=[]
        for a in V:
            U.append(a.nombre)
        lista=[]
        for a in U:            
            u=G.getNodo(a)
            if u.color == "Blanco":
                lista2=[]
                lista.append(lista2)
                G.DFS_Visit(u,lista2)
        return lista
        
  


      