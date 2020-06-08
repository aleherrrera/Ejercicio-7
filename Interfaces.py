from zope.interface import Interface

class IConjunto(Interface):

    def insertarElemento(posicion,agente):
        pass

    def agregarElemento(posicion,agente):
        pass

    def mostrarElemento(posicion):
        pass
    