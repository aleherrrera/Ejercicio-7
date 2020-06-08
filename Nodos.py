class Nodo(object):
    __agente=None
    __siguente=None

    def __init__(self,agente):
        self.__agente=agente
        self.__siguente=None

    def setSiguiente(self,siguiente):
        self.__siguente=siguiente
    def getSiguiente(self):
        return self.__siguente
    def getDato(self):
        return self.__agente