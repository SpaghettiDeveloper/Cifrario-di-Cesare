#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Crypton - Cifrario di Cesare
## Linguaggio: Python 3.5
## Autore: Stefano Peris <SpaghettiDeveloper>
## Licenza: GPL/GNU 2016

def caesar_cypher():
    try:
        inp=raw_input("Inserire stringa: ")
    except:
        print("Errore!")
    try:
        key=input("Inserire chiave: ")
    except:
        print("Errore!")
    y=len(inp)
    print "La lunghezza della stringa e': ", y
    b=""
    for i in range(len(inp)):
        b += chr(ord(inp[i]) + key)
    print b
