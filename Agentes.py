class Personal(object):
    __cuil=0
    __apellido=''
    __nombre=''
    __sueldoBasico=0.0
    __antiguedad=0

    def __init__(self,cuil, apellido, nombre, basico, antiguedad,
                 area,tipo,clases,cargo,catedra,categoria,categoriaInv,
                 impDocenecia,impoInves):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldoBasico=basico
        self.__antiguedad=antiguedad

    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNom(self):
        return self.__nombre
    def getBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def Info(self):
        print('\nDATOS PERSONALES')
        cadena = 'CUIL: %d\nNombre y Apellido: %s\nSueldo Basico:$%.2f\nAntiguedad: %d'% \
                 (self.__cuil, self.__str__(),self.__sueldoBasico,self.__antiguedad)
        return cadena

    def __str__(self):
        cadena='%s %s'% (self.__nombre,self.__apellido)
        return cadena