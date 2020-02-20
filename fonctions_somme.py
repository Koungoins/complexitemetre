from labels import *
from variables_g import *
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
  tab = data[abscisses]
  for sel in selection :
    tmp = []
    for d in tab :
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
            tmp.append(t)
    points[sel] = tmp
  return points