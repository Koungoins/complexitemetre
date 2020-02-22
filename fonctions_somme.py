#!/bin/env python
# coding=utf-8

from labels import *
import time
#Fichiers contenant tout les variables
import variables_g as varsG

import statistics as stats


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
    rep = 0
    releves = []
    found = False
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
                print("Key trop grand:", d)
                continue

            #Recupère la clé dans la liste des abscisses
            if not d in varsG.keys_utiles :
                varsG.keys_utiles.append(d)

            rep = 0
            #Lance la fonction avec les memes parametres plusieurs fois faire une moyenne
            while rep < varsG.passages :
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
                  releves.append(t)
                rep += 1

            if found :
                #Moyenne pour des relevés
                moyenne = stats.mean(releves)
                varsG.points[sel].append(moyenne)
