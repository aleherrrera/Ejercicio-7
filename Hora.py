
class Hora:
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self,hora=0,min=0,seg=0):
        self.__hora = hora
        self.__minutos = min
        self.__segundos = seg

    def __str__(self):
        return '{}:{}:{}'.format(self.__hora,self.__minutos,self.__segundos)

    def Mostrar(self):
        s = 'HORA MIN SEG\n'
        print('{}{}:{}:{}'.format(s,self.__hora,self.__minutos,self.__segundos))

    def getH(self):
        return self.__hora

    def getM(self):
        return self.__minutos

    def getS(self):
        return self.__segundos


