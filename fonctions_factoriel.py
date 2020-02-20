from labels import *
from variables_g import *
import time


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
def runMesure(selection, data) :
  t = 0
  found = False
  points = {}
  tab = data[abscisses]
  for sel in selection :
    tmp = []
    for d in tab :
      t = time.time()

      if sel == nom_factoriel_iteratif :
        factorielIteratif(d)
        found = True
      elif sel == nom_factoriel_recursif :
        factorielRecursif(d)
        found = True
      else :
        found = False

      t = time.time() - t
      if found :
        tmp.append(t)
    points[sel] = tmp
  return points