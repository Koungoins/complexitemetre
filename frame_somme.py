#!/bin/env python
# coding=utf-8

from tkinter import *

#Fichier contenant tout les textes
from labels import *
from fonctions_somme import *

#Fichiers contenant les variables
import variables_g as varsG


class PanelSomme :

  #Listner du bouton choix des fonctions à lancer
  def valide_choix(self, *args) :
    self.selection = []
    if self.chkValue3.get() :
      self.selection.append(nom_somme_formule)
    if self.chkValue1.get() :
      self.selection.append(nom_somme_iteratif)
    if self.chkValue2.get() :
      self.selection.append(nom_somme_recursif)
    runMesure(self.selection)
    self.mainF.tracerCourbes()



  def __init__(self, p, mainF) :
    self.parent = p
    self.mainF = mainF
    self.matrices = {}
    self.selection = []
    self.panelPrincipale = PanedWindow(self.parent, width = 200, height = 400, orient = VERTICAL)
    self.panelPrincipale['bg'] = 'white'

    self.chkValue3 = BooleanVar()
    self.choix3 = Checkbutton(self.panelPrincipale, text = nom_somme_formule, variable = self.chkValue3)
    self.choix3.select()
    self.choix3['bg'] = 'white'
    self.choix3.pack()

    self.chkValue1 = BooleanVar()
    self.choix1 = Checkbutton(self.panelPrincipale, text = nom_somme_iteratif, variable = self.chkValue1)
    self.choix1.select()
    self.choix1['bg'] = 'white'
    self.choix1.pack()

    self.chkValue2 = BooleanVar()
    self.choix2 = Checkbutton(self.panelPrincipale, text = nom_somme_recursif, variable = self.chkValue2)
    self.choix2.select()
    self.choix2['bg'] = 'white'
    self.choix2.pack()

    self.bouton_valide = Button(self.panelPrincipale, text = label_valider)
    self.bouton_valide.pack()

    self.bouton_valide['command'] = self.valide_choix
    self.panelPrincipale.pack()