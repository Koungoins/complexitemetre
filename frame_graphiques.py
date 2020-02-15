# coding=utf-8
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

#Fichier contenant tout les textes
from labels import *
from fonctions_somme import *

#Fichiers contenant les variables
from variables_g import *


class PanelGraphiques :
		


  def __init__(self, p, pointsX, pointsY, mainF) :
    self.parent = p
    self.mainF = mainF
    self.graphique = g
    self.matrices = {}
    self.selection = []
    self.data = d
    self.points = points
    self.panelPrincipale = PanedWindow(self.parent, width = 200, height = 400, orient = VERTICAL)
    self.panelPrincipale['bg'] = 'green'
    self.panelPrincipale.pack()