#-*- coding: utf-8 -*-
"""
 :description :Analizador léxico para expresiones aritméticas       
 :author :Luis Pablo Mayo Vega
 :note :Compiladores 2017-2
"""

from plex import *

# Especificación de los patrones asociados a los tokens
letra = Range("AZaz")
digito = Range("09")
varid = letra + Rep(letra | digito)
numero = (Rep1(digito)) | (Rep1(digito) + Str(".") + Rep1(digito))
espacios = Any(" \t\n")

lex = Lexicon([
    (varid, 'VAR_ID'),
    (numero, 'NUMERO'),
    (Str("+"), 'OP_SUMA'),
    (Str("-"), 'OP_RESTA'),
    (Str("*"), 'OP_MULT'),
    (Str("/"), 'OP_DIV'),
    (Str("="), 'ASIG'),
    (Str("("), 'PARIZQ'),
    (Str(")"), 'PARDER'),
    (Str(";"), 'SEMICOLON'),
    (espacios, IGNORE)
])

def get_tokens(filename):
    tokens = []
    f = open(filename, 'r')
    scanner = Scanner(lex, f, filename)
    while True:
        tok = scanner.read()
        if (tok[0] is None):
            break
        tokens.append(tok)
    return tokens

#tokens = get_tokens("prueba.txt")
