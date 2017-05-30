#-*- coding: utf-8 -*-
"""
 :description :clase Visitor que nos permite evaluar el ASA        
 :author :Luis Pablo Mayo Vega
 :note :Compiladores 2017-2
"""
class Visitor:
    """
    Clase 'abstracta' para el patrón de diseño Visitor
    """
    def __init__(self):
        raise NotImplementedError("Esta clase no implementa ninguna función")
    def visitNodoNum(self, nodo_num):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoSuma(self, nodo_suma):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoResta(self, nodo_resta):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoMult(self, nodo_mult):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoDiv(self, nodo_div):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoParIzq(self, nodo_par_izq):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoParDer(self, nodo_par_der):
        raise NotImplementedError("Esta clase no implementa ninguna función")
    
    def visitNodoAsig(self, nodo_asig):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoPuntoComa(self, nodo_pyc):
        raise NotImplementedError("Esta clase no implementa ninguna función")

class VisitorInterp(Visitor):
    """
    Clase visitor para el interprete
    """
    def __init__(self):
        """
        Inicializa el resultado de la interpretación en 0.
        Además, crea una tupla para la variable y su valor.
        """
        res = 0
        ident = ''
        var_tup = ()
        parizq_count = 0
        parder_count = 0
        
    def visitNodoNum(self, nodo_num):
        """
        Visita un nodo de número y guarda su valor en el resultado
        """
        self.res = nodo_num.value

    def visitNodoVar(self, nodo_var):
        """
        Visita un nodo de variable y guarda su identificador
        """
        self.ident = nodo_var.varid 
    def visitNodoSuma(self, nodo_suma):
        """
        Visita un nodo suma y evalua los valores de sus hijos izq y der,
        Guarda el resultado de la evaluación en la variable res.
        """
        nodo_suma.izq.accept(self)
        res_izq = self.res
        nodo_suma.der.accept(self)
        res_der = self.res
        self.res = res_izq + res_der

    def visitNodoResta(self, nodo_resta):
        """
        Visita un nodo resta y evalua los valores de sus hijos izq y der,
        Guarda el resultado de la evaluación en la variable res.
        """
        nodo_resta.izq.accept(self)
        res_izq = self.res
        nodo_resta.der.accept(self)
        res_der = self.res
        self.res = res_izq - res_der

    def visitNodoMult(self, nodo_mult):
        """
        Visita un nodo multiplica y evalua los valores de sus hijos izq y der,
        Guarda el resultado de la evaluación en la variable res.
        """
        nodo_mult.izq.accept(self)
        res_izq = self.res
        nodo_mult.der.accept(self)
        res_der = self.res
        self.res = res_izq * res_der

    def visitNodoDiv(self, nodo_div):
        """
        Visita un nodo división y evalua los valores de sus hijos izq y der,
        Guarda el resultado de la evaluación en la variable res.
        """
        nodo_div.izq.accept(self)
        res_izq = self.res
        nodo_div.der.accept(self)
        res_der = self.res
        self.res = res_izq / res_der
        
    def visitNodoAsig(self, nodo_asig):
        """
        Visita un nodo de asignación y guarda la variable
        y su valor correspondiente que están en sus hijos
        """
        nodo_asig.izq.accept(self)
        iden = self.ident
        nodo_asig.izq.accept(self)
        valor = self.res
        self.var_tup = (iden, valor)
        
        def visitNodoParIzq(self, nodo_par_izq):
            # idk wat 2 do with dis 1
            parizq_count += 1

        def visitNodoParDer(self, nodo_par_der):
            parder_count  += 1

        def visitNodoPuntoComa(self, nodo_pyc):
            pass # hmmm
        
class VisitorPrint(Visitor):
    pass    
