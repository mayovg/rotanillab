#-*- coding: utf-8 -*-
"""
 :description :Analizador sintáctico para expresiones aritméticas       
 :author      :Luis Pablo Mayo Vega
 :note        :Compiladores 2017-2
"""
import sys
from plex import *
from scanner import Lexer

class Parser:
    """
    Clase para el analizador sintáctico
    """
    def __init__(self, tokens):
        """
        Inicializador de los objetos Parser 
        param: una lista de tokens 
        """
        self.tokens = tokens
        self.nodes_queue = []
        
    def start(self):
        """
        Acepta la cadena de entrada si es un programa válido para la grámatica:
        S -> Prog
        """       
        if(prog(self) or len(self.tokens) is 0):
            return True
        else:
            return False

    def prog(self):
        """
        Evalua que que la entrada sea una expresión aritmética o una asignación:
        Prog -> Expr 
        """
        if (expr(self) or asig(self)):
            return True
        else:
            return False

    def asig(self):
        pass

    def asigp(self):
        pass
        
    def expr(self):
        pass

    def exprp(self):
         pass

    def term(self):
        pass

    def termp(self):
        pass

    def fact(self):
        pass  

    def error(self):
        raise Exception('Lo siento, no te entendí')
    
# pequeña prueba
lexer = Lexer()
if (len(sys.argv) > 1):
    tokens = lexer.get_tokens(sys.argv[1])
else:
    tokens = lexer.get_tokens("prueba.txt")
print tokens
