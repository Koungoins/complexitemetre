# coding=utf-8
from tkinter import *

#Fichier contenant tout les textes
from labels import *
from fonctions_recherche import *

#Fichiers contenant les variables
from variables_g import *


class PanelRecherche :

  #Listner du bouton choix des fonctions à lancer
  def valide_choix(self, *args) :
    if self.chkValue1.get() :
      self.selection.append(nom_rechercher_naif)
    if self.chkValue2.get() :
      self.selection.append(nom_rechercher_dico)
    print("Data rech:",self.data)
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
    self.choix1 = Checkbutton(self.panelPrincipale, text = nom_rechercher_naif, variable = self.chkValue1)
    self.choix1.select()
    self.choix1.pack()

    self.chkValue2 = BooleanVar()
    self.choix2 = Checkbutton(self.panelPrincipale, text = nom_rechercher_dico, variable = self.chkValue2)
    self.choix2.select()
    self.choix2.pack()

    self.bouton_valide = Button(self.panelPrincipale, text = label_valider)
    self.bouton_valide.pack()

    self.bouton_valide['command'] = self.valide_choix
    self.panelPrincipale.pack()