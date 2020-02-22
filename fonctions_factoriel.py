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

  varsG.points = {}
  varsG.keys_utiles = []
  for sel in selection :
    found = False
    varsG.points[sel] = []
    #repasse plusieurs fois
    releves = []
    for d in varsG.keys :
        #Evite de faire les clés qui pourraient faire bugger les recursions
        if mot_recursif in str(selection) and d > varsG.max_recurences :
            #print("Key trop grand:", d)
            continue

        #Recupère la clé dans la liste des abscisses
        if not d in varsG.keys_utiles :
            varsG.keys_utiles.append(d)

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
