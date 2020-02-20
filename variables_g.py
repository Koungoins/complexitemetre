#!/bin/env python
# coding=utf-8

#Fichier contenant tout les textes
from labels import *
import json


choix_fonctions = [nom_somme, nom_factoriel, nom_maximum, nom_rechercher, nom_tris]
choix_fonction_selected = nom_somme

#Liste des données
dico = {}
points = {}
dico['abscisses'] = [1, 10, 20, 50, 70, 100, 150, 200, 300, 500,1000, 1500, 2000, 10000, 100000]
data = 1000
abscisses = 'abscisses'
t1 = dico[abscisses]
dico[abscisses] = t1
dataKey = 'data'
dico[dataKey] = {}
colorsPlots = ['b','g','r','y']
data_file = 'datafile.txt'


def writeDataFile() :
	with open(data_file,'w') as outfile :
	   json.dump(dico, outfile)



def readDataFile() :
	with open(data_file) as json_file :
		dico = json.load(json_file)
		#print("Lire json:",dico)



#Génère automatiquement une liste de données
def genereDataListe(*args) :
  for taille in t1 :
    #print("Taille:",taille)
    dico[dataKey][taille] = []
    for i in range(taille) :
      #dico[taille].append(int(random.random()*data))
      dico[dataKey][taille].append(i + 1)
    #print(dico)
  writeDataFile()





  #print("Dico ",dico)