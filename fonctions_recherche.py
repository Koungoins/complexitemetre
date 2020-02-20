from labels import *
from variables_g import *
import time


#Recherche un element n et renvoi sa position dans la liste  ou -1 s'il n'existe pas dans la liste
def rechercherNaif(n, liste) :
    print("Liste Rechercher:",liste)
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
def runMesure(selection, data) :
    e = 10000000
    t = 0
    found = False
    points = {}
    tab = data[abscisses]
    for sel in selection :
        tmp = []
        for d in tab :
            t = time.time()
            if sel == nom_rechercher_naif :
                rechercherNaif(e, tab[d])
                found = True
            elif sel == nom_rechercher_dico :
                rechercheDicho(e, tab[d])
                found = True
            t = time.time() - t
            if found :
                tmp.append(t)
    points[sel] = tmp
    return points