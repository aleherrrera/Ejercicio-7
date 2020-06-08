from Agentes import Personal

class Investigador(Personal):
    __areaInvestigacion=''
    __tipoInvestigacion=''

    def __init__(self,cuil, apellido, nombre, basico, antiguedad,area,
                 tipo,clases=0,cargo='',catedra='',categoria=0,categoriaInv='',
                 impDocenecia=0.0,impoInves=0.0):
        super().__init__(cuil, apellido, nombre, basico, antiguedad,
                         area,tipo,clases,cargo,catedra,categoria,categoriaInv,
                 impDocenecia,impoInves)
        self.__areaInvestigacion=area
        self.__tipoInvestigacion=tipo

    def getArea(self):
        return self.__areaInvestigacion

    def getSueldo(self):
        antiguedad=self.getBasico()*(self.getAntiguedad()*0.01)
        sueldoInvestigador = self.getBasico()+ antiguedad
        return sueldoInvestigador

    def Info(self):
        print(super().Info())
        print('DATOS INVESTIGADOR')
        cadena='Area de Investigacion: %s\nTipo de Investigacion: %s'%\
               (self.__areaInvestigacion,self.__tipoInvestigacion)
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
                area=self.__areaInvestigacion,
                tipo=self.__tipoInvestigacion
            )
        )
        return d