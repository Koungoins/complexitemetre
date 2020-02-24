#!/bin/env python
# coding=utf-8

#Fichier contenant tout les textes
from labels import *
import json
import threading
import time


choix_fonctions = [nom_somme, nom_factoriel, nom_rechercher, nom_tris, nom_fibo]
choix_fonction_selected = nom_somme

#Liste des données
dico = {'keys':[1, 10, 20, 50, 70, 100, 150, 200, 300]}#, 500, 700, 800, 1000, 1500, 3000, 3500, 4000, 10000]}

keys = dico['keys']
keys_utiles = []
data = {}
points = {}
element = 10000000
max_recurences = 970
millisec = 1000
fonction_selected = None

#Nombre de passages sur la même fonction pour avoir un temps moyenne excecution
passages = 5

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
    data = {}
    for taille in keys :
        data[taille] = []
        for i in range(taille) :
          #dico[taille].append(int(random.random()*x))
          data[taille].append(i + 1)
    dico['data'] = data
    writeDataFile()
    data = dico['data']





  #print("Dico ",dico)