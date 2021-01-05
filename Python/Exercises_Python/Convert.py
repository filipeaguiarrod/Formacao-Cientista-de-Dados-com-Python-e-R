# -*- coding: utf-8 -*-
"""
Created on Sat May 16 13:53:16 2020

@author: rodri
"""


def convertmile(m):
    m=float(m)
    # 1 mile = 1,609344 kilometes
    km = 1,609344*m
    
    return(km,"Km")

def convertemp(c):
    f=((c*9)/5)+32
    return(f,"Fº")

# Decimal to bynary
    
def convertbin(n):
    n=int(n)
    bin=[]
    binary=""
    while n > 2: # n=25
        b=n%2
        print("b :", b)
        bin.append(b)
        n=n//2
        print("n :",n)
    bin.append(1)
    bin.reverse()
    for i in bin:
        binary += str(i)       
    return("You binary numb is: ", binary)    
