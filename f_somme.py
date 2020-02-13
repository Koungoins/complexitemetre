# script spinbox.py
#(C) Fabrice Sincère
# coding=utf-8
from tkinter import *

#Fichier contenant tout les textes
from labels import *

#Fichiers contenant les variables
from variables_g import *


class PanelSomme :

    #Listner du bouton choix des fonctions à lancer
    def valide_choix(self, *args) :
    	print("Bouton appuyé")



    def __init__(self, p) :
        self.parent = p
        self.panelPrincipale = PanedWindow(self.parent, width = 200, height = 400, orient = VERTICAL)
        self.panelPrincipale['bg'] = 'blue'
        #self.parent.add(self.panelPrincipale)

        self.choix3 = Checkbutton(self.panelPrincipale, text = nom_somme_formule)
        self.choix3.pack()

        self.choix1 = Checkbutton(self.panelPrincipale, text = nom_somme_iteratif)
        self.choix1.pack()

        self.choix2 = Checkbutton(self.panelPrincipale, text = nom_somme_recursif)
        self.choix2.pack()

        self.bouton_valide = Button(self.panelPrincipale, text = label_valider)
        self.bouton_valide.pack()

        self.bouton_valide['command'] = self.valide_choix
        self.panelPrincipale.pack()