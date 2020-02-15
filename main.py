# coding=utf-8
import random

from tkinter import *
from tkinter import ttk
#Fichier contenant tout les textes
from labels import *

#Fichiers contenant tout les variables
from variables_g import *


#Les fenetres
from frame_somme import *
from frame_factoriel import *
from frame_maxi import *
from frame_recherche import *
from frame_tris import *

#Les fonctions
from fonctions_somme import *
from fonctions_factoriel import *
from fonctions_maximum import *
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
        self.f_choix_teste['bg'] = 'grey'
        self.f_choix_teste.pack(side = LEFT, padx = 3, pady = 3)

        #Panel graphique
        self.f_graphique = PanedWindow(self.panelContener, width = 600, height = 400)
        self.f_graphique['bg'] = 'yellow'
        self.f_graphique.pack(side = RIGHT, padx = 3, pady = 3)

        #Graphiques dans un canvas
        self._fig = Figure(figsize=(5,4))
        self._ax = self._fig.add_subplot(111) 
        self._canvas = FigureCanvasTkAgg(self._fig, master=self.f_graphique)        
        self._canvas.get_tk_widget().pack( side=TOP, fill=BOTH, expand=1)        
        self._canvas.draw()


        #Affichage de la fenetre
        self.fenetre.mainloop()

    #Listener de composants
    #Listener de la combo choix de fonctions
    def choix_fonction(self, *args):
        if self.liste_fonctions.get() == nom_somme :
            self.panelSomme = PanelSomme(self.f_choix_teste, dico, points, self)
    
    def tracerCourbes(self, *args) :
      print("Retour :",args[0])         
      d = args[0]      
      i = 0
      for nom in d.keys() :
        self._ax.plot(t1, args[0][nom], colorsPlots[i])
        i = i + 1

      self._canvas.draw()


    def genereDataListe(*args) :
      
      data = 1000
      for taille in t1 :
        #print("Taille:",taille)
        dico[taille]=[]
        for i in range(taille) :
          dico[taille].append(int(random.random()*data))
        #print(dico)
      #print("Dico ",dico)


    genereDataListe()
    #genereDataListe(self)

f = MainFrame()

