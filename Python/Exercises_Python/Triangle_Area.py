# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:39:32 2020

@author: rodri
"""


def triangarea(a,b,c):
    
    
    import math
    
       
    a=float(a)
    b=float(b)
    c=float(c)
    
    s=(a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
               
    print (area)
                
    
triangarea(10,10,10)
  


# Prime number is not divisible by any numbers between 1 and the n itself

def primenum(n):
    
    for i in range (2,n):
        if n%i==0:
            #print("It's not a prime number")
            break
    print("Nice, It's a prime number !")
            
        
            
primenum(1783)
    
#User will give the number and the program will find all primer number up to thins number:

n = input("Give me some number...")
n=int(n)
for j in range (0,n+1):
    print(j)
    primenum(j)

primenum(1)