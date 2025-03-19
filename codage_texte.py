# -*- coding: utf-8 -*-
"""
Created on 09/11/2019
@author: alaeddine ben rhouma
"""
from random import *

alphabet=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
 ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8',
  '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E',
   'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
     'z', '{', '|', '}', '~', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨',
     '©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶',
      '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã',
       'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð',
        'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý',
         'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê',
          'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷',
           'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ']

# Fonction qui concatène à un caractère donné, k caractères
#aléatoires de la liste alphabet

def concatene(c,k):
    l=len(alphabet)
    for i in range(k):
        c=c+choice(alphabet)
    return c

#Compter le nombre de lignes dans le fichier cles.txt
cles=open('cles.txt', 'r')
n = 0
while cles.readline():
    n += 1
cles.close()

#Extraire aléatoirement une clé du fichier cles.txt
m=randint(1,n)
cles=open('cles.txt', 'r')
k=1
while k<m:
    cle=cles.readline()
    k=k+1
cles.close()

#Transformation de la clé en liste
cle=cle.split(" ")

#Extraire le numéro de la clé qui est le premier élément de la liste cle
num=cle[0]

#Extraire la clé de chiffrement avec suppression du dernier élément de la liste clé qui est le symbole "\n"
cle=cle[1:-1]

#Transformer la clé en liste d'entiers
for k in range(len(cle)):
    cle[k]=int(cle[k])


##################CHIFFREMENT###############################

#création d'un fichier texte qui contiendra le texte chiffré

chiff=open("albatros_chiffre.txt","w")

#Ecrire le numéro de la clé sur une ligne
chiff.write(num)
chiff.write("\n")

# Ouverture du texte clair
clair=open("albatros.txt","r")



k=0
while 1:
    char=clair.read(1)
    if not char:
         break

    char=concatene(char,cle[k])
    k=(k+1)%(len(cle))
    chiff.write(char)


#Fermeture des fichiers

clair.close()
chiff.close()




