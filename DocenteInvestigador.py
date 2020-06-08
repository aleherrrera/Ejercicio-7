from Docente import Docente
from Investigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __categoriaInvestigacion=''
    __importeDocencia=0.0
    __importeInvestigacion=0.0

    def __init__(self,cuil, apellido, nombre, basico, antiguedad,clases,cargo,catedra,area,tipo,
                 categoriaInv,importeD,importeI,categoria=0):
        super().__init__(cuil,apellido,nombre,basico,antiguedad,clases,
                         cargo,catedra,area,tipo,categoria,categoriaInv,importeD,importeI)
        self.__categoriaInvestigacion=categoriaInv
        self.__importeDocencia=importeD
        self.__importeInvestigacion=importeI

    def getCatInvestigacion(self):
        return self.__categoriaInvestigacion
    def getImporteD(self):
        return self.__importeDocencia
    def getImporteI(self):
        return self.__importeInvestigacion

    def getSueldo(self):
        antiguedad = self.getBasico() * (self.getAntiguedad() * 0.01)
        if self.getCargo().lower() == 'simple':
            cargo = self.getBasico() * 0.1
        else:
            if self.getCargo().lower() == 'semiexclusivo':
                cargo = self.getBasico() * 0.2
            else:
                if self.getCargo().lower() == 'exclusivo':
                    cargo = self.getBasico() * 0.5
        sueldoDocente = self.getBasico() + antiguedad + cargo
        sueldoDocenteInvestigador =sueldoDocente+ self.__importeInvestigacion + self.__importeDocencia
        return sueldoDocenteInvestigador

    def Info(self):
        print(super().Info())
        print('DATOS DOCENE/INVESTIGADOR')
        cadena='Categoria de Investigacion: %s\nImporte extra docencia: $%.2f\nImporte extra investigacion: $%.2f' \
               '\nSueldo Total: $%.2f'%\
               (self.__categoriaInvestigacion,self.__importeDocencia,self.__importeInvestigacion,self.getSueldo())
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
                clases=self.getClases(),
                cargo=self.getCargo(),
                catedra=self.getCatedra(),
                area=self.getArea(),
                tipo=self.getTipo(),
                categoriaInv=self.__categoriaInvestigacion,
                importeD=self.__importeDocencia,
                importeI=self.__importeInvestigacion
            )
        )
        return d