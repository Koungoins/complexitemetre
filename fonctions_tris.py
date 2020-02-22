#!/bin/env python
# coding=utf-8

from labels import *
import threading as thread
import time
#Fichiers contenant tout les variables
import variables_g as varsG

import statistics as stats


def triSelection(tab) :
  for i in range(len(tab)):
    # Trouver le min
    min = i
    for j in range(i+1, len(tab)):
      if tab[min] > tab[j]:
        min = j
    #deplace le min
    tmp = tab[i]
    tab[i] = tab[min]
    tab[min] = tmp
  return tab



def triInsertion(tab) :
  # Parcour de 1 à la taille du tab
  for i in range(1, len(tab)):
    k = tab[i]
    j = i-1
    while j >= 0 and k < tab[j] :
      tab[j + 1] = tab[j]
      j -= 1
    tab[j + 1] = k
  return ta


def triBulle(tab) :
  n = len(tab)
  # Traverser tous les éléments du tableau
  for i in range(n):
    for j in range(0, n-i-1):
      # échanger si l'élément trouvé est plus grand que le suivant
      if tab[j] > tab[j+1] :
        tab[j], tab[j+1] = tab[j+1], tab[j]
  return tab


def triRapide(tab) :
  i1, i2, n1, n2 = 0, 0, len(t1), len(t2)
  t = []
  while i1 < n1 and i2 < n2 :
    if t1[i1] < t2[i2] :
      t.append(t1[i1])
      i1 += 1
    else :
      t.append(t2[i2])
    i2 += 1
  if i1 == n1 :
    t.extend(t2[i2:])
  else :
    t.extend(t1[i1:])
  return t



#fonction qui execute les mesures
def runMesure(selection) :
  t = 0
  rep = 0
  varsG.points = {}
  varsG.keys_utiles = varsG.keys
  for sel in selection :
    print
    found = False
    varsG.points[sel] = []
    #repasse plusieurs fois
    releves = []
    for d in varsG.keys :
        rep = 0
        #Lance la fonction avec les memes parametres plusieurs fois faire une moyenne
        while rep < varsG.passages :
            t = time.time()
            if sel == nom_tri_bulle :
                triBulle(varsG.data[d])
                found = True
            elif sel == nom_tri_selection :
                triSelection(varsG.data[d])
                found = True
            elif sel == nom_tri_insertion :
                triSelection(varsG.data[d])
                found = True
            elif sel == nom_tri_rapide :
                triSelection(varsG.data[d])
                found = True

            t = time.time() - t
            if found :
                releves.append(t)
            rep += 1

        if found :
            #Moyenne pour des relevés
            moyenne = stats.mean(releves)
            varsG.points[sel].append(moyenne)

#fonction qui execute les mesures
#def runMesure(selection) :
 #   t = thread.Thread(target = mesure, args = (selection,))
  #  t.start()