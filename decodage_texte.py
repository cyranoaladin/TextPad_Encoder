# -*- coding: utf-8 -*-
"""
Created on 09/11/2019
@author: alaeddine ben rhouma
"""

#Ouverture du texte chiffré en mode lecture
texte_chiffre=open("albatros_chiffre.txt","r")

#Extraire le numéro de la clé qui se trouve sur la première
#ligne du texte chiffré
num=texte_chiffre.readline()

#Transformer le type de num en entier
num=int(num)

#Ouvrir le fichier cles.txt en mode lecture
cles=open("cles.txt","r")

#Lecture de la clé numéro num
for k in range(num):
    cle=cles.readline()

#Transformer la ligne extraite en liste
cle=cle.split(" ")

#Supprimer le numéro de la clé (premier élément)
#et le caractère "\n" (dernier élément)
cle=cle[1:-1]

#Transformer la liste cle en liste d'entiers
for k in range(len(cle)):
    cle[k]=int(cle[k])

#Création d'un fichier qui va contenir le texte déchiffré
#en mode écriture
texte_dechiffre=open("albatros_dechiffre.txt","w")

#Déchiffrement et écriture en parcourant le texte
#et en utilisant la liste cle d'une manière cyclique
k=0
while 1:
    char=texte_chiffre.read(1)
    if not char:
         break
    texte_dechiffre.write(char)

    char=texte_chiffre.read(cle[k])
    k=(k+1)%(len(cle)) # permet de revenir au début de la liste  lorsqu'on arrive au dernier élément



#Fermeture de tous les fichiers

texte_chiffre.close()
texte_dechiffre.close()
cles.close()
