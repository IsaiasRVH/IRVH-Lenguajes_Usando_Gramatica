# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:47:19 2021

@author: Isaías Ricardo Valdivia Hernández

Σ = { a, b ,c} 

L3: Todas las cadenas con no más de tres  a’s

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
        return True
    
def A(word, i):
    if i < len(word):
        if word[i] == 'b' or word[i] == 'c':
            return A(word, i + 1)
        elif word[i] == 'a':
            return B(word, i + 1)
    else:
        return True
    

def B(word, i):
    if i < len(word):
        if word[i] == 'b' or word[i] == 'c':
            return B(word, i + 1)
        elif word[i] == 'a':
            return C(word, i + 1)
    else:
        return True
    
def C(word, i):
    if i < len(word):
        if word[i] == 'b' or word[i] == 'c':
            return C(word, i + 1)
        elif word[i] == 'a':
            return False
    else:
        return True
    
word = input('Ingrese una palabra: ')

if(analize(word)):
    print(word + ' pertenece al lenguaje')
else:
    print(word + ' no pertenece al lenguaje')