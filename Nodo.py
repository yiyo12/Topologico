#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:13:42 2020

@author: lbeltran
"""

class Nodo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.adjunta = []
        self.d= 0
        self.f= 0
        self.padre = None
        self.color = "Blanco"
        
    def show(self):
        print(self.nombre,"(",self.d,"/", self.f, ")", end=" ")
        for i in self.adjunta:
            print(i.nombre, end=" ")
        print("")
        
    def addAdyacente(self,A):
        self.adjunta.append(A)
        
        