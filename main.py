# script spinbox.py
#(C) Fabrice Sincère
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




#Declaration des variables de l'interface


#Listener de composants
#Listener de la combo choix de fonctions
def choix_fonction(event):
    choix_fonction_selected = liste_fonctions.get()
    print(choix_fonction_selected)









#Déclaration de la fenetre
fenetre = Tk()
fenetre['bg']='white'
fenetre.configure(width=800,height=600)
fenetre.title(titre_fenetre)

#Panel combobox choix fonctions
f_combo_choix = PanedWindow(fenetre, width=800,height=50, orient=HORIZONTAL)
f_combo_choix['bg']='red'
f_combo_choix.pack(side=TOP, padx=3,pady=3)

#Nom de la comboBox choix de la fonction
label_nom_comboBox = Label(f_combo_choix, text="Choix fonction : ", padx=2)
label_nom_comboBox.pack(side=LEFT)

#Liste de fonctions choix
liste_fonctions = ttk.Combobox(f_combo_choix, values=choix_fonctions)
#liste_fonctions.configure(state='readonly')
liste_fonctions.pack(side=LEFT)
#Selection du premier élément de la liste
liste_fonctions.current(0)
#Listener pour faire une action lors de la sélection d'un élément dans la liste
liste_fonctions.bind("<<ComboboxSelected>>", choix_fonction)


#Panel checkBox choix mesure
f_combo_choix = PanedWindow(fenetre, width=200,height=600, orient=VERTICAL)
f_combo_choix['bg']='grey'

f_combo_choix.pack(side=LEFT, padx=3,pady=3)
bouton_valide = Button(f_combo_choix, text="Valider")
bouton_valide.pack(side=BOTTOM)

#Listner du bouton choix des fonctions à lancer
def valide_choix() :
    print("Bouton appuyé")
    #f_combo_choix.add(createPanelSomme(f_combo_choix))

bouton_valide['command'] = valide_choix


#Panel graphique
f_combo_choix = PanedWindow(fenetre, width=600,height=600)
f_combo_choix['bg']='yellow'
f_combo_choix.pack(side=RIGHT, padx=3,pady=3)

#Affichage de la fenetre
fenetre.mainloop()






