#!/bin/env python
# coding=utf-8

from labels import *
import time
#Fichiers contenant tout les variables
import variables_g as varsG

import statistics as stats

def factorielIteratif(n) :
  produit = 1
  i = n
  while i >= 1 :
    produit = produit * i
    i = i - 1
  return produit



def factorielRecursif(n) :
  if n == 1 :
    return 1
  else :
    return n * factorielRecursif(n-1)



#fonction qui execute les mesures
def runMesure(selection) :
  t = 0
  rep = 0
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
            if sel == nom_factoriel_iteratif :
                factorielIteratif(d)
                found = True
            elif sel == nom_factoriel_recursif :
                factorielRecursif(d)
                found = True

            t = time.time() - t
            if found :
                releves.append(t)
            rep += 1

        if found :
		  #Moyenne pour des relevés
            moyenne = stats.mean(releves)
            varsG.points[sel].append(moyenne)