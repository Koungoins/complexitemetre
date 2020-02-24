#!/bin/env python
# coding=utf-8

from labels import *
import threading as thread
import time
#Fichiers contenant tout les variables
import variables_g as varsG

import statistics as stats


def triSelection(tabl) :
  tmp = 0
  jMin = 0
  j = 0
  for i in range(len(tabl)-1) :
    j = i
    jMin = j
    #Recherche du min
    while j < len(tabl) :
      if tabl[j]<tabl[jMin] :
        jMin = j
      j = j + 1

    #Echange de place si min different de i
    if jMin != i :
      tmp = tabl[i]
      tabl[i]=tabl[jMin]
      tabl[jMin] = tmp
      #print("Liste:", liste)
  return tabl



def triInsertion(liste) :
  i = 1
  iTemp = 0
  j = 0
  n = 0
  while i < len(liste) :
    iTemp = liste[i]
    #print("iTemp:",iTemp)
    j = i - 1
    #Recherche du plus petit
    while j >= 0 :
      #print("recherche:",j)
      if liste[j] < iTemp :
        j = j + 1
        petit = True
        break
      j = j - 1
    #Pas de plus petit, on met au début
    if j < 0 :
      j = 0
    #print("Place:",liste[j])

    #Deplacement
    n = i
    while n >= j :
      #print("n:",n,", j:",j)
      liste[n] = liste[n - 1]
      #print("dep:",liste)
      n = n - 1
    #print("iTemp repl:",iTemp)
    #Mise en tete
    liste[j] = iTemp
    #print("Liste nouv :",liste)
    i = i + 1
  return liste


def triBulle(tabl) :
  tmp = 0
  changement = False
  for i in range(len(tabl)-1) :
    if tabl[i] > tabl[i+1] :
      tmp = tabl[i]
      tabl[i] = tabl[i+1]
      tabl[i+1] = tmp
      changement = True
  if changement :
    triBulle(tabl)
  return tabl


def fusion(a, b) :
    c = []
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < len(a) and j < len(b) : # on continue tant que les deux listes ne sont pas vides
    	if a[i] < b[j] :
            c.append(a[i])
            i = i + 1
    	else :
            c.append(b[j])
            j = j + 1
    # ‡ ce stade, une (au moins) des deux listes est vide, et on ajoute les ÈlÈments de líautre liste ‡ c
    if i == len(a) :
    	for j in range(j,len(b)) :
            print("ici 2")
            c.append(b[j])
    else :
    	for j in range(i,len(a)) :
            print("ici 3")
            c.append(a[i])
    return c

def triRapide(a) : # il síagit ici díune fonction renvoyant la liste des ÈlÈments de a triÈs
    print("ici 11")
    n = len(a)
    if n <= 1 :
        return a
    m = n // 2
    # on utilise ensuite le ìslicingî pour dÈÖnir les sous-listes, on les trie et on renvoie leur fusion :
    return fusion( triFusion(a[0:m]) , triFusion(a[m:n]) )


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
                triInsertion(varsG.data[d])
                found = True
            elif sel == nom_tri_rapide :
                print("Debut fonction")
                triRapide(varsG.data[d])
                found = True

            t = time.time() - t
            if found :
                releves.append(t)
            rep += 1

        if found :
            #Moyenne pour des relevés
            moyenne = stats.mean(releves)
            varsG.points[sel].append(moyenne*varsG.millisec)

#fonction qui execute les mesures
#def runMesure(selection) :
 #   t = thread.Thread(target = mesure, args = (selection,))
  #  t.start()