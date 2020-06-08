from Agentes import Personal

class Apoyo(Personal):
    __categoria=0

    def __init__(self,cuil, apellido, nombre, basico, antiguedad,categoria,
                area='',tipo='',clases=0,cargo='',catedra='',categoriaInv='',
                 impDocenecia=0.0,impoInves=0.0):
        super().__init__(cuil, apellido, nombre, basico, antiguedad,area,tipo,
                         clases,cargo,catedra,categoria,categoriaInv,impDocenecia,impoInves)
        self.__categoria=categoria

    def getSueldo(self):
        antiguedad = self.getBasico() * (self.getAntiguedad() * 0.01)
        a=[1,2,3,4,5,6,7,8,9,10]
        b=[11,12,13,14,15,16,17,18,19,20]
        c=[21,22]
        if self.__categoria in a:
            categoria = self.getBasico() * 0.1
        else:
            if self.__categoria in b:
                categoria = self.getBasico() * 0.2
            else:
                if self.__categoria in c:
                    categoria = self.getBasico() * 0.3
        sueldoPersonalDeApoyo = self.getBasico() + antiguedad + categoria
        return sueldoPersonalDeApoyo

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNom(),
                basico=self.getBasico(),
                antiguedad=self.getAntiguedad(),
                categoria=self.__categoria,
            )
        )
        return d
