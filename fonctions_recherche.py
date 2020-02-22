#!/bin/env python
# coding=utf-8

from labels import *
import threading as thread
import time
#Fichiers contenant tout les variables
import variables_g as varsG

import statistics as stats

#Recherche un element n et renvoi sa position dans la liste  ou -1 s'il n'existe pas dans la liste
def rechercherNaif(n, liste) :
  i = 0
  while i <= len(liste) - 1 :
    if liste[i] == n :
      return i
    i = i + 1
  return -1


#Recherche dichotomoque d'un élément dans une liste
def rechercheDicho(e, tab) :
  trouve = False
  debut = 0
  milieu = 0
  fin = len(tab) - 1
  while trouve == False and debut <= fin :
    milieu = int((debut + fin) / 2)
    if tab[milieu] == e :
      trouve = True
    else :
      if e > tab[milieu] :
        debut = milieu + 1
      else :
        fin = milieu - 1
  return trouve


#fonction qui execute les mesures
def runMesure(selection) :
  t = 0
  rep = 0
  varsG.points = {}
  varsG.keys_utiles = varsG.keys
  for sel in selection :
    found = False
    varsG.points[sel] = []
    #repasse plusieurs fois
    releves = []
    for d in varsG.keys :
        rep = 0
        #Lance la fonction avec les memes parametres plusieurs fois faire une moyenne
        while rep < varsG.passages :
            t = time.time()
            if sel == nom_rechercher_naif :
                rechercherNaif(varsG.element, varsG.data[d])
                found = True
            elif sel == nom_rechercher_dico :
                rechercheDicho(varsG.element, varsG.data[d])
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