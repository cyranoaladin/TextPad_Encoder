# -*- coding: utf-8 -*-

texte=open("texte_clair.txt","r")
while 1:
    char = texte.read(1)          # Lire le fichier caractère
    if not char:
         break
    print (char)
texte.close()


k=0
m=3
cles=open('cles.txt', 'r')
while k<m:
    cle=cles.readline()
    k=k+1
cles.close()

#Transformation de la clé en liste
cle=cle.split(" ")
