from Hora import Hora

class FechaHora:

    __dia = 0
    __mes = 0
    __anio = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self,dia=1,mes=1,anio=2020,hora=0,minuto=0,segundo=0):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__hora = hora
        self.__minutos = minuto
        self.__segundos = segundo

    def __str__(self):
        return '{}/{}/{}/  {}:{}:{}'.format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos)

    def Mostrar(self):

        if self.getSeg() > 59:
            self.__segundos = self.getSeg() - 60
            self.__minutos += 1
        else:
            self.__segundos = self.getSeg()
        if self.getMin() > 59:
            self.__minutos = self.getMin() - 60
            self.__hora += 1
        else:
            self.__minutos = self.getMin()
        if self.getHora() > 23:
            self.__hora = self.getHora() - 24
            self.__dia += 1
            m = self.Mes(self.__mes)
            if self.__dia > m:
                self.__mes += 1
                if self.__mes > 12:
                    self.__anio += 1
        else:
            self.__hora = self.getHora()

        if self.getSeg() < 0:
            self.__segundos = self.getSeg() + 60
            self.__minutos -= 1
        else:
            self.__segundos = self.getSeg()
        if self.getMin() < 0:
            self.__minutos = self.getMin() + 60
            self.__hora -= 1
        else:
            self.__minutos = self.getMin()
        if self.getHora() < 0:
            self.__hora = self.getHora() + 24
            self.__dia -= 1
            print(self.getDia())
            if self.getDia() == 0:
                self.__mes -= 1
                if self.getMes() == 0:
                    self.__mes = 12
                    print()
                    self.__anio -= 1
                    m = self.Mes(self.__mes)
                    self.__dia = m
        else:
            self.__hora = self.getHora()

        s = 'DIA/MES/AÑO    HORA:MIN:SEG\n'
        print('{}{}/{}/{}          {}:{}:{}'.format(s,self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos))

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAnio(self):
        return self.__anio

    def getHora(self):
        return self.__hora

    def getMin(self):
        return self.__minutos

    def getSeg(self):
        return self.__segundos

    def Bisiesto(self,anio):
        m = anio%4
        if m == 0:
            m = anio%100
            if m == 0:
                m = anio%400
                if m == 0:
                    return 29
                else:
                    return 28

    def Mes(self,mes):
        if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            return 31
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            return 30
        else:
            a = self.Bisiesto(self.__anio)
            return a

    def __add__(self, hora):
        return FechaHora(self.__dia,self.__mes,self.__anio,self.__hora + hora.getH(),self.__minutos + hora.getM(),self.__segundos + hora.getS())

    def __radd__(self, hora):
        if type(hora)==Hora:
            return FechaHora(self.__dia,self.__mes,self.__anio,self.__hora + hora.getH(),self.__minutos + hora.getM(),self.__segundos + hora.getS())
        else:
            if type(hora)==int:
                return FechaHora(self.__dia + hora,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos)

    def __sub__(self, hora):
        return FechaHora(self.__dia - hora,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos)