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
        self.word = ()
    def start(self):
        """
        Acepta la cadena de entrada si es un programa válido para la grámatica:
        S -> Prog
        """
        word = tokens.pop(0)
        #nodes_queue.append(Nodo(word))
        if(prog(self) or len(self.tokens) is 0):
            return True
        else:
            return False

    def prog(self):
        """
        Evalua que la entrada sea una expresión aritmética o una asignación:
        Prog -> Expr 
        """
        if (expr(self) or asig(self)):
            return True
        else:
            return False

    def asig(self):
        if (self.word[0] is 'VARIABLE'):
            nodes_queue.append(NodoVar(word))
            word = tokens.pop(0)
            return asigp(self)
        else:
            error(self)

    def asigp(self):
        if (self.word[0] is 'ASIG'):
            nodes_queue.append(NodoAsig(word))
            word = tokens.pop(0)
            if (expr(self)):
                return True
            else:
                error(self)
            
    def expr(self):
        if (term(self)):
            return eprime(self)
        else:
            error(self)

    def eprime(self):
        if (self.word[0] is 'OP_SUMA' or self.word[0] is 'OP_RESTA'):
            if (self.word[0] is 'OP_RESTA'):
                nodes_queue.append(NodoResta(word))
            nodes_queue.append(NodoSuma(word))
            word = tokens.pop(0)
            if (term(self)):
                return eprime(self)
            else:
                error(self)
        elif (self.word[0] is 'PARDER' or word[0] is 'eof'):
            return True
        else:
            error(self)

    def term(self):
        if (factor(self)):
            return tprime(self)
        else:
            error(self)

    def tprime(self):
        if (self.word[0] is 'OP_MULT' or self.word[0] is 'OP_DIV'):
            word = tokens.pop(0)
            if (factor(self)):
                return tprime(self)
            else:
                error(self)
        elif (self.word[0] is 'OP_SUMA' or self.word[0] is 'OP_RESTA'
              or self.word[0] is 'PARDER' or self.word[0] is 'eof'):
            return True
        else:
            error(self)

    def fact(self):
        if (self.word[0] is 'PARIZQ'):
            word = tokens.pop(0)
            if (not expr(self)):
                error(self)
            if (word[0] is not 'PARDER'):
                error(self)
            word = tokens.pop(0)
            return True

    def error(self):
        raise Exception('Lo siento, no te entendí')
    
# pequeña prueba
lexer = Lexer()
if (len(sys.argv) > 1):
    tokens = lexer.get_tokens(sys.argv[1])
else:
    tokens = lexer.get_tokens("prueba.txt")
print tokens
