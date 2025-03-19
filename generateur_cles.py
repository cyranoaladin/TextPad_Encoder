"""
Created on 09/11/2019
@author: alaeddine ben rhouma
"""

from random import *

NombreCles=100
Min=6
Max=8
DecaleMax=10

cles=open("cles.txt","w")
for i in range(NombreCles):
    long=randint(Min,Max)
    cles.write(str(i+1)+" ")
    for k in range(long):
        cles.write(str(randint(1,DecaleMax))+" ")
    cles.write("\n")
cles.close()



