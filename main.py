# coding=utf-8
from tkinter import *
from tkinter import ttk

#Fichier contenant tout les textes
from labels import *

#Fichiers contenant les variables
from variables_g import *


#Les fenetre
from f_somme import *
from f_factoriel import *
from f_maxi import *
from f_recherche import *
from f_tris import *

#Les fonction
from fonctions_somme import *
from fonctions_factoriel import *
from fonctions_maximum import *
from fonctions_recherche import *
from fonctions_tris import *


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


        #Affichage de la fenetre
        self.fenetre.mainloop()

    #Listener de composants
    #Listener de la combo choix de fonctions
    def choix_fonction(self, *args):
        if self.liste_fonctions.get() == nom_somme :
            self.panelSomme = PanelSomme(self.f_choix_teste,self.f_graphique)

f = MainFrame()