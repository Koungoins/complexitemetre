#!/bin/env python
# coding=utf-8

from tkinter import *

#Fichier contenant tout les textes
from labels import *
from fonctions_tris import *

#Fichiers contenant les variables
from variables_g import *


class PanelTris :

  #Listner du bouton choix des fonctions à lancer
  def valide_choix(self, *args) :

    self.selection = []
    if self.chkValue1.get() :
      self.selection.append(nom_tri_bulle)
    if self.chkValue2.get() :
      self.selection.append(nom_tri_selection)
    if self.chkValue3.get() :
      self.selection.append(nom_tri_insertion)
    if self.chkValue4.get() :
      self.selection.append(nom_tri_rapide)
    runMesure(self.selection)
    self.mainF.tracerCourbes()


  def __init__(self, p, mainF) :

    self.parent = p
    self.mainF = mainF
    self.matrices = {}
    self.selection = []
    self.panelPrincipale = PanedWindow(self.parent, width = 200, height = 400, orient = VERTICAL)
    self.panelPrincipale['bg'] = 'white'

    self.chkValue1 = BooleanVar()
    self.choix1 = Checkbutton(self.panelPrincipale, text = nom_tri_bulle, variable = self.chkValue1)
    self.choix1.select()
    self.choix1['bg'] = 'white'
    self.choix1.pack()

    self.chkValue2 = BooleanVar()
    self.choix2 = Checkbutton(self.panelPrincipale, text = nom_tri_selection, variable = self.chkValue2)
    self.choix2.select()
    self.choix2['bg'] = 'white'
    self.choix2.pack()

    self.chkValue3 = BooleanVar()
    self.choix3 = Checkbutton(self.panelPrincipale, text = nom_tri_insertion, variable = self.chkValue3)
    self.choix3.select()
    self.choix3['bg'] = 'white'
    self.choix3.pack()

    self.chkValue4 = BooleanVar()
    self.choix4 = Checkbutton(self.panelPrincipale, text = nom_tri_rapide, variable = self.chkValue4)
    self.choix4.select()
    self.choix4['bg'] = 'white'
    self.choix4.pack()

    self.bouton_valide = Button(self.panelPrincipale, text = label_valider)
    self.bouton_valide.pack()

    self.bouton_valide['command'] = self.valide_choix
    self.panelPrincipale.pack()