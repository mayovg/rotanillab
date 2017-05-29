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

# Especificación del lexicón para los lexemas
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
    """
    Regresa una lista con todos los tokens de un archivo de entrada.
    Para obtener cada token de dicho archivo, usa un Scanner de Plex,
    este scanner usa su funcion read() para buscar lexemas en el archivo 
    """
    tokens = []
    f = open(filename, 'r')
    scanner = Scanner(lex, f, filename)
    while True:
        tok = scanner.read()
        if (tok[0] is None):
            break
        tokens.append(tok)
    return tokens

