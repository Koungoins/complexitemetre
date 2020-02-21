#!/bin/env python
# coding=utf-8
import random
import json

from tkinter import *
from tkinter import ttk
#Fichier contenant tout les textes
from labels import *

#Fichiers contenant tout les variables
import variables_g as varsG


#Les fenetres
from frame_somme import *
from frame_factoriel import *
from frame_fibonacci import *
from frame_recherche import *
from frame_tris import *

#Les fonctions
from fonctions_somme import *
from fonctions_factoriel import *
from fonctions_fibonacci import *
from fonctions_recherche import *
from fonctions_tris import *

#Import pour le graphique
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np



class MainFrame  :

    #Declaration des variables de l'interface
    def __init__(self) :
        #Déclaration de la fenetre
        self.fenetre = Tk()
        self.fenetre['bg'] = 'white'
        self.fenetre.configure(width = 800, height = 800)
        self.fenetre.title(titre_fenetre)

        #Panel combobox choix fonctions
        self.f_combo_choix = PanedWindow(self.fenetre, width = 780, height = 50, orient = HORIZONTAL)
        self.f_combo_choix['bg']='red'
        self.f_combo_choix.pack(side = TOP, padx = 3, pady = 3)

        #Nom de la comboBox choix de la fonction
        self.label_nom_comboBox = Label(self.f_combo_choix, text = l_choix_fonction, padx = 2)
        self.label_nom_comboBox.pack()

        #Liste de fonctions choix
        self.liste_fonctions = ttk.Combobox(self.f_combo_choix, values = choix_fonctions)
        self.liste_fonctions.configure(state='readonly')
        self.liste_fonctions.pack()
        #Selection du premier élément de la liste
        #self.liste_fonctions.current(0)
        #Listener pour faire une action lors de la sélection d'un élément dans la liste
        self.liste_fonctions.bind("<<ComboboxSelected>>", self.choix_fonction)

        self.panelContener = PanedWindow(self.fenetre, width = 800, height = 400)
        self.panelContener['bg']='pink'
        self.panelContener.pack()

        #Panel checkBox choix mesure
        self.f_choix_teste = PanedWindow(self.panelContener, width = 100, height = 400, orient = VERTICAL)
        self.f_choix_teste['bg'] = 'green'
        self.f_choix_teste.pack(side = LEFT, padx = 3, pady = 3)


        #Panel contener Graphiques
        self.paneContenerG = PanedWindow(self.panelContener, width = 600, height = 400, orient = VERTICAL)
        self.paneContenerG.pack()
        self.paneContenerG['bg'] = 'black'

        #Panel des options
        self.paneOptions = PanedWindow(self.paneContenerG, width = 600, height = 150)
        self.paneOptions.pack()
        self.paneOptions['bg'] = 'grey'

        #Panel graphique
        self.f_graphique = PanedWindow(self.paneContenerG, width = 600, height = 300)
        self.f_graphique['bg'] = 'yellow'
        self.f_graphique.pack(side = RIGHT, padx = 3, pady = 3)

        #self._fig = None
        #if self._fig != None :
        #self._fig.clear()
        #Graphiques dans un canvas
        self._fig = Figure(figsize = (5, 4))
        self._ax = self._fig.subplots()
        self._ax.legend(loc = 'best')
        self._canvas = FigureCanvasTkAgg(self._fig, master = self.f_graphique)
        self._canvas.get_tk_widget().pack( side = TOP, fill = BOTH, expand = 1)
        self._canvas.draw()

        #Affichage de la fenetre
        self.fenetre.mainloop()

    #Listener de composants
    #Listener de la combo choix de fonctions
    #Permet de créer le panel de gauche avec la fonction selectionnée
    def choix_fonction(self, *args) :

        #Efface l'encienne fonction dans les choix
        for widget in self.f_choix_teste.winfo_children() :
            widget.destroy()

        if self.liste_fonctions.get() == nom_somme :
            self.panelSomme = PanelSomme(self.f_choix_teste,  self)

        if self.liste_fonctions.get() == nom_rechercher :
            self.panelSomme = PanelRecherche(self.f_choix_teste, self)

        if self.liste_fonctions.get() == nom_factoriel :
            self.panelSomme = PanelFactoriel(self.f_choix_teste, self)

        if self.liste_fonctions.get() == nom_tris :
            self.panelSomme = PanelTris(self.f_choix_teste, self)

        if self.liste_fonctions.get() == nom_fibo :
            self.panelSomme = PanelFibo(self.f_choix_teste, self)



    #Tracer la courbe avec les points
    def tracerCourbes(self, *args) :
      print("Retour :")
      print("points keys:", varsG.points.keys())
      print(" keys:", varsG.keys)
      i = 0
      for nom in varsG.points.keys() :
        self._ax.plot(varsG.keys, varsG.points[nom], varsG.colorsPlots[i])
        self._canvas.draw()
        i += 1


    varsG.genereDataListe()
    varsG.data = varsG.dico['data']
    #print("data:", varsG.data)
    #genereDataListe(self)
    #print(rechercherNaif(10, dico[t1[3]]))

f = MainFrame()
#varsG.genereDataListe()
