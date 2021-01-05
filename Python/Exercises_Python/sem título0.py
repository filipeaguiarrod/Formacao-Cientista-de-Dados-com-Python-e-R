# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:29:44 2020

@author: rodri
"""

# You borrowed $5000 for 2 years with 2% interest per year
# Simple interest, how to pay?


#J = C.i.t

C=input("How Many have you been borrowed ?")
C=float(C)
i=(2/100)
t=input("How many time you intend to pay ?")
t=float(t)
J=C*i*t
print("You need pay",J,"interest taxes")

#Compound Interest 
#A=P(1+R/100)^t

C=input("How Many have you been borrowed ?")
C=float(C)
i=(2/100)
t=input("How many time you intend to pay ?")
t=float(t)
M = C*(1+i)**t
print("You need pay",M,"interest taxes")