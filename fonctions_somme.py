#!/bin/env python
# coding=utf-8

from labels import *
import time


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
def runMesure(selection, data) :
  t = 0
  found = False

  points = {}
  
  for sel in selection :    
    points[sel] = []
    for d in data.keys() :
      #print("Key=",d)
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
      else :
        found = False
      
      t = time.time() - t
      if found :      
        points[sel].append(t)
  #print("Point", points)
  return points