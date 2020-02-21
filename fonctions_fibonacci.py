from labels import *
from variables_g import *
import time
#!/bin/env python
# coding=utf-8

from labels import *
import time
#Fichiers contenant tout les variables
import variables_g as varsG

import statistics as stats


#Fibo en iteratif
def fiboIteratif(n) :
    a = 0
    b = 1
    if n == 0 :
        return a
    elif n == 1 :
        return b
    else :
        for i in range(2, n) :
            c = a + b
            a = b
            b = c
        return b


#Fibo en récursif
def fiboRecursif(n) :
    if n == 1 :
        return 0
    elif n == 2 :
        return 1
    else :
        return fiboRecursif(n-1)+fiboRecursif(n-2)

#fonction qui execute les mesures
def runMesure(selection) :
  t = 0
  rep = 0
  releves = []
  found = False
  varsG.points = {}
  for sel in selection :
    varsG.points[sel] = []
    #repasse plusieurs fois
    releves = []
    for d in varsG.keys :
      rep = 0
	  #Lance la fonction avec les memes parametres plusieurs fois faire une moyenne
      while rep < varsG.passages :
        t = time.time()
        if sel == nom_fibo_iteratif :
          fiboIteratif(d)
          found = True
        elif sel == nom_fibo_recursif :
          fiboRecursif(d)
          found = True

        t = time.time() - t
        if found :
          releves.append(t)
        rep += 1

      if found :
		#Moyenne pour des relevés
        moyenne = stats.mean(releves)
        varsG.points[sel].append(moyenne)
