#-*- coding: utf-8 -*-
"""
 :description :Analizador léxico para expresiones aritméticas       
 :author :Luis Pablo Mayo Vega
 :note :Compiladores 2017-2
"""

from plex import *

class Lexer:
    """
    Clase para el analizador léxico 
    """
    def __init__(self):
        # Especificación de los patrones asociados a los tokens
        letra = Range("AZaz")
        digito = Range("09")
        variable = letra + Rep(letra | digito)
        numero = (Rep1(digito)) | (Rep1(digito) + Str(".") + Rep1(digito))
        operador = Str('+') | Str('-') | Str('*') | Str('/')
        op_bin = numero + operador + numero 
        op_un = operador + numero 
        espacios = Any(" \t\n")
        
        # Especificación del lexicón para los lexemas
        self.lex = Lexicon([
            (variable, 'VARIABLE'),
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

    def get_tokens(self,filename):
        """
        Regresa una lista con los tokens de un archivo de entrada.
        Para obtener cada token del archivo, usa un Scanner de Plex,
        este scanner usa su funcion read() para buscar los lexemas  
        """
        tokens = []
        f = open(filename, 'r')
        scanner = Scanner(self.lex, f, filename)
        while True:
            tok = scanner.read()
            if (tok[0] is None):
                break
            tokens.append(tok)
        return tokens
        
        
