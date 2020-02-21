#!/bin/env python
# coding=utf-8

#Fichier contenant tout les textes
from labels import *

choix_fonctions = [nom_somme, nom_factoriel, nom_maximum, nom_rechercher, nom_tris]
choix_fonction_selected = nom_somme

#Liste des données
dico = {'keys':[1, 10, 20, 50, 70, 100, 150, 200, 300, 500,1000, 1500]}
keys = dico['keys']
data = {}
points = {}
#Nombre de passages sur la même fonction pour avoir une moyenne
passages = 5

colorsPlots = ['b','g','r','y']


#Génère automatiquement une liste de données
def genereDataListe(*args) :    
  for taille in keys :    
    data[taille] = []
    for i in range(taille) :
      #dico[taille].append(int(random.random()*x))
      data[taille].append(i + 1)  
  dico['data'] = data
  #print("Dico ",dico)