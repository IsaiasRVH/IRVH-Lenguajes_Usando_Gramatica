# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:30:15 2021

@author: Isaías Ricardo Valdivia Hernández

Σ = { a, b ,c} 

L1: Todas las cadenas con una  a exactamente

"""

def analize(word):
    i = 0
    return S(word, i)
    
    
def S(word, i):
    if i < len(word):
        if word[i] == 'b' or word[i] == 'c':
            return S(word, i + 1)
        elif word[i] == 'a':
            return A(word, i + 1)
    else:
        return False
    
def A(word, i):
    if i < len(word):
        if word[i] == 'b' or word[i] == 'c':
            return B(word, i + 1)
        else:
            return False
    else:
        return True

def B(word, i):
    if i < len(word):
        if word[i] == 'b' or word[i] == 'c':
            return B(word, i + 1)
        elif word[i] == 'a':
            return False
    else:
        return True
    

word = input('Ingrese una palabra: ')

if(analize(word)):
    print(word + ' pertenece al lenguaje')
else:
    print(word + ' no pertenece al lenguaje')