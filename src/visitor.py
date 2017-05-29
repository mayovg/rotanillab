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
    def visitNodoNum(self, nodo_num):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoSuma(self, nodo_suma):
        raise NotImplementedError("Esta clase no implementa ninguna función")

    def visitNodoAsig(selfm nodo_asig):
        raise NotImplementedError("Esta clase no implementa ninguna función")

class VisitorInterp(Visitor);
pass

class VisitorPrint(Visitor):
pass    
