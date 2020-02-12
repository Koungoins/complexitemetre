# script spinbox.py
#(C) Fabrice Sincère
# coding=utf-8
from tkinter import *

#Fichier contenant tout les textes
from labels import *

#Fichiers contenant les variables
from variables_g import *

def createPanelSomme(parent) :
    panelPrincipale = PanedWindow(parent, width=200,height=400, orient=VERTICAL)
    panelPrincipale['bg']='blue'
    #choix1 = Checkbutton(panelPrincipale, text=nom_somme_iteratif)
    #choix1.pack()
    panelPrincipale.pack()
    return panelPrincipale
