#-*- coding: utf-8 -*-
"""
 :description :clase Nodo para el Árbol de Análisis Sintáctico       
 :author :Luis Pablo Mayo Vega
 :note :Compiladores 2017-2
"""
import Visitor

class Nodo:
    """
    Clase padre para los nodos del árbol
    """
    def __init__(self, token):
        """
        Cada nodo del árbol, tiene un nodo hijo izquierdo y uno derecho,
        aunque en un principio lo consideramos una 'hoja'.
        también se le asigna un token generado por el analizador léxico 
        """
        self.izq = None
        self.der = None
        self.token = token
    
    def tipo(self):
        """
        Regresa el tipo del token en el nodo.
        --------------------------------------------------------
        Los tokens son tuplas de la forma: (value, text), pero 
        en esta implementación el valor se refiere al tipo y 
        el texto es un elemento de la entrada que coincide 
        con el patrón dado para el tipo
        
        """
        return self.token[0]
    
    def set_izq(self, nodo):
        """
        Le asigna un nuevo hijo izquierdo al nodo        
        """
        self.izq = nodo

    def set_der(self, nodo):
        """
        Le asigna un nuevo hijo derecho al nodo
        """
        self.der = nodo

    def __str__(self):
        """
        Regresa una representación en cadena del árbol
        """
        d = depth(self) + 1 # calcula la profundidad del árbol
        branch = [] # designa si se dibujan ramas o espacios
        for i in range(0, p):
            branch[i] = False # al principio no se dibuja ninguna rama
        s = toString(self, 0, branch):
        return s[:-1]

    def toString(self, lev, branch):
        """
        Función auxiliar que dibuja el árbol recursivamente
        """
        s = self.token[1] + "\n" # agrega el simbolo en el nodo actual
        branch[lev] = True
        # comprueba que el nodo tenga hijo izquierdo y derecho
        if (self.izq is not None and self.der is not None):
            s+= spaces(self, lev, branch) # dibujamos espacios o ramas
            s += "├─›" # dibuja el conecto al hijo izquierdo
            s += toString(self.izq, lev+1, branch) # dibuja el hijo izq
            s += spaces(self, lev, branch) 
            s += "└─»" # dibuja el conector al hijo derecho
            branch[lev] = False # ya no hay ramas en este nivel
            s += toString(self.der, lev+1, branch) # dibuja al hijo der
        elif (self.izq is not None): # solo hay hijo izquierdo
            s += spaces(self, lev, branch)
            s += "└─»"
            branch[lev] = False
            s += toString(self.izq, lev+1, branch)
        elif (self.der is not None):
            s += "└─»"
            branch[lev] = False
            s += toString(self.der, lev+1, branch)
        return s

    def spaces(self, level, branch):
        """
        Dibuja los espacios y ramas que van antes de un nodo
        """
        s = ""
        for i in range (0. level):
            if (branch[i]):
                s += "│  " # si hay una rama la dibuja
            else:
                s += "   "
            return s

    def depth(self):
        """
        Regresa la profundidad del árbol
        """
        ld = -1 # profundidad del subarbol izquierdo
        rd = -1 # profundidad del subárbol derecho
        if (self.izq is not None):
            # si hay hijo izquierdo, calcula su profundidad
            ld = depth(self.izq) 
        if(self.der is not None):
            # si hay hijo derecho, calcula su profundidad
            rd = depth(self.der)
        # compara las profundidades y regresa la mayor
        if (ld > rd):
            return ld + 1
        else:
            return rd + 1
        
        

class NodoNum(Nodo):
    """
    Clase nodo para valores númericos
    """
    def __init__(self,token):
        """
        Usa el constructor de su clase padre
        """
        Nodo.__init__(self,token)
