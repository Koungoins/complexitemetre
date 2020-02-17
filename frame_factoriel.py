# coding=utf-8
from tkinter import *

#Fichier contenant tout les textes
from labels import *
from fonctions_factoriel import *

#Fichiers contenant les variables
from variables_g import *


class PanelFactoriel :

  #Listner du bouton choix des fonctions à lancer
  def valide_choix(self, *args) :
    
    if self.chkValue1.get() :      
      self.selection.append(nom_factoriel_iteratif)
    if self.chkValue2.get() :      
      self.selection.append(nom_factoriel_recursif)
    self.points = runMesure(self.selection, self.data)    
    self.mainF.tracerCourbes(self.points)
		


  def __init__(self, p, d, points, mainF) :
    self.parent = p
    self.mainF = mainF    
    self.matrices = {}
    self.selection = []
    self.data = d
    self.points = points
    self.panelPrincipale = PanedWindow(self.parent, width = 200, height = 400, orient = VERTICAL)
    self.panelPrincipale['bg'] = 'blue'

    self.chkValue1 = BooleanVar()
    self.choix1 = Checkbutton(self.panelPrincipale, text = nom_factoriel_iteratif, variable = self.chkValue1)
    self.choix1.select()
    self.choix1.pack()

    self.chkValue2 = BooleanVar()
    self.choix2 = Checkbutton(self.panelPrincipale, text = nom_factoriel_recursif, variable = self.chkValue2)
    self.choix2.select()
    self.choix2.pack()

    self.bouton_valide = Button(self.panelPrincipale, text = label_valider)
    self.bouton_valide.pack()

    self.bouton_valide['command'] = self.valide_choix
    self.panelPrincipale.pack()