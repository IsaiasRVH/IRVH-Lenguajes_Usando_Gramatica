# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:20:48 2021

@author: Isaías Ricardo Valdivia Hernández

Σ = { a, b ,c} 

L5: El lenguaje que contiene la subpalabra bcac

"""

def analize(word):
    i = 0
    return S(word, i)
    
    
def S(word, i):
    if i < len(word):
        if word[i] == 'a' or word[i] == 'c':
            return S(word, i + 1)
        elif word[i] == 'b':
            return A(word, i + 1)
    else:
        return False
    
def A(word, i):
    if i < len(word):
        if word[i] == 'a':
            return S(word, i + 1)
        elif word[i] == 'b':
            return A(word, i + 1)
        elif word[i] == 'c':
            return B(word, i + 1)
    else:
        return False

def B(word, i):
    if i < len(word):
        if word[i] == 'a':
            return C(word, i + 1)
        elif word[i] == 'b':
            return A(word, i)
        elif word[i] == 'c':
            return S(word, i + 1)
    else:
        return False

def C(word, i):
    if i < len(word):
        if word[i] == 'a':
            return S(word, i + 1)
        elif word[i] == 'b':
            return A(word, i)
        elif word[i] == 'c':
            return D(word, i + 1)
    else:
        return False

def D(word, i):
    if i < len(word):
        if word[i] == 'a' or word[i] == 'b' or word[i] == 'c':
            return D(word, i + 1)
    else:
        return True
    
word = input('Ingrese una palabra: ')

if(analize(word)):
    print(word + ' pertenece al lenguaje')
else:
    print(word + ' no pertenece al lenguaje')