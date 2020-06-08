from Agentes import Personal

class Docente(Personal):
    __clases=0
    __cargo=''
    __catedra=''

    def __init__(self, cuil, apellido, nombre, basico, antiguedad,
                 clases, cargo, catedra, area='', tipo='',categoria=0,categoriaInv='',
                 impDocenecia=0.0,impoInves=0.0):
        super().__init__(cuil, apellido, nombre, basico, antiguedad,area,tipo,
                         clases,cargo,catedra,categoria,categoriaInv,
                         impDocenecia,impoInves)
        self.__clases=clases
        self.__cargo=cargo
        self.__catedra=catedra

    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra

    def getSueldo(self):
        antiguedad=self.getBasico()*(self.getAntiguedad()*0.01)
        if self.__cargo.lower()=='simple':
            cargo= self.getBasico()*0.1
        else:
            if self.__cargo.lower() == 'semiexclusivo':
                cargo = self.getBasico()*0.2
            else:
                if self.__cargo.lower() == 'exclusivo':
                    cargo = self.getBasico()*0.5
        sueldoDocente = self.getBasico()+ antiguedad + cargo
        return sueldoDocente

    def Info(self):
        print(super().Info())
        print('DATOS DOCENTE')
        cadena='Clases: %d\nCargo: %s\nCatedra: %s'%\
               (self.__clases,self.__cargo,self.__catedra)
        return cadena

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNom(),
                basico=self.getBasico(),
                antiguedad=self.getAntiguedad(),
                clases=self.__clases,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d