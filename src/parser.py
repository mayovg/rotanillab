#-*- coding: utf-8 -*-
"""
 :description :Analizador sintáctico para expresiones aritméticas       
 :author      :Luis Pablo Mayo Vega
 :note        :Compiladores 2017-2
"""
import sys
from plex import *
from scanner import *

def accept(tokens):
    """
    Acepta la cadena de entrada si es un programa válido para la grámatica:
    S -> Prog
    """ 
    if(prog(tokens) or len(tokens) is 0):
            return True
    else:
        return False


def prog(tokens):
    """
    Evalua que que la entrada sea una expresión aritmética o una asignación:
    Prog -> Expr 
    """
    if (expr(tokens) or asig(tokens)):
        return True
    else:
        return False
    
    
def expr(tokens):
    pass

if (len(sys.argv) > 1):
    tokens = get_tokens(sys.argv[1])
else:
    tokens = get_tokens("prueba.txt")

for t in tokens:
    print t[1]
