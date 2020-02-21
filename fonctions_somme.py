#!/bin/env python
# coding=utf-8

from labels import *
import time
#Fichiers contenant tout les variables
import variables_g as varsG


#Somme avec une formaule
def sommeFormule(n) :
    return n * (n + 1) / 2


#Somme en iteratif
def sommeIteratif(n) :
  somme = 0
  i = n
  while i >= 0 :
    somme = somme + i
    i = i -1 
  return somme


#Somme en récursif
def sommeRecursif(n) :
  if n == 0 :
    return 0
  else :
    return n + sommeRecursif(n - 1)



#fonction qui execute les mesures
def runMesure(selection) :
  t = 0
  found = False
  varsG.points = {}  
  for sel in selection :    
    varsG.points[sel] = []
    for d in varsG.keys :      
      t = time.time()
      if sel == nom_somme_formule :               
        sommeFormule(d)
        found = True
      elif sel == nom_somme_iteratif :
        sommeIteratif(d)
        found = True
      elif sel == nom_somme_recursif :
        sommeRecursif(d)
        found = True
      
      t = time.time() - t
      if found :      
        varsG.points[sel].append(t)  
    