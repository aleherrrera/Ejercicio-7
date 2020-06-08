from zope.interface import implementer
from Interfaces import IConjunto
from Nodos import Nodo
from Docente import Docente
from Investigador import Investigador
from Apoyo import Apoyo
from DocenteInvestigador import DocenteInvestigador

@implementer(IConjunto)

class ListaAgentes(object):
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def crear(self):
        opcion = int(input('Tipo de personal\n1=Docente\n2=Investigador\n'
                           '3=Personal de apoyo\n4=Docente investigador\n'
                           'Ingresar opcion: '))
        if opcion == 1:
            cuil=int(input('Ingresar CUIL: '))
            apellido=str(input('Ingresar apellido: '))
            nombre=str(input('Ingrese nombre: '))
            basico=float(input('Ingrese sueldo basico: '))
            antiguedad=int(input('Ingrese antiguedad: '))
            clases=int(input('Ingrese clases: '))
            cargo=str(input('Ingrese cargo(simple/semiexclusivo/exclusivo): '))
            catedra=str(input('Ingrese catedra: '))
            agente=Docente(cuil,apellido,nombre,basico,antiguedad,clases,cargo,catedra)
        else:
            if opcion == 2:
                cuil = int(input('Ingresar CUIL: '))
                apellido = str(input('Ingresar apellido: '))
                nombre = str(input('Ingrese nombre: '))
                basico = float(input('Ingrese sueldo basico: '))
                antiguedad = int(input('Ingrese antiguedad: '))
                area = str(input('Ingrese area de investigacion: '))
                tipo = str(input('Ingrese tipo de investigacion: '))
                agente = Investigador(cuil, apellido, nombre, basico, antiguedad, area, tipo)
            else:
                if opcion == 3:
                    cuil = int(input('Ingresar CUIL: '))
                    apellido = str(input('Ingresar apellido: '))
                    nombre = str(input('Ingrese nombre: '))
                    basico = float(input('Ingrese sueldo basico: '))
                    antiguedad = int(input('Ingrese antiguedad: '))
                    categoria = int(input('Ingrese categoria(1-2-3-4-...-22): '))
                    agente = Apoyo(cuil, apellido, nombre, basico, antiguedad,categoria)
                else:
                    if opcion == 4:
                        cuil = int(input('Ingresar CUIL: '))
                        apellido = str(input('Ingresar apellido: '))
                        nombre = str(input('Ingrese nombre: '))
                        basico = float(input('Ingrese sueldo basico: '))
                        antiguedad = int(input('Ingrese antiguedad: '))
                        clases = int(input('Ingrese clases: '))
                        cargo = str(input('Ingrese cargo(simple/semiexclusivo/exclusivo): '))
                        catedra = str(input('Ingrese catedra: '))
                        area = str(input('Ingrese area de investigacion: '))
                        tipo = str(input('Ingrese tipo de investigacion: '))
                        categoria=str(input('Ingresar categoria de investigacion((I, II, III, IV o V)): '))
                        importeD=float(input('Ingrese importe de docencia: '))
                        importeI=float(input('Ingrese importe de investigacion: '))
                        agente = DocenteInvestigador(cuil, apellido, nombre, basico, antiguedad, clases, cargo,
                                                     catedra,area, tipo,categoria, importeD, importeI)
                    else:
                        raise ValueError
        return agente

    def cargar(self,agente=None):
        if agente ==None:
            agente=self.crear()
        nodo = Nodo(agente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual=nodo
        self.__tope+=1

    def insertarElemento(self,posicion,agente):
        if posicion>=0 and posicion < self.__tope:
            aux = self.__comienzo
            if posicion==0:
                if agente!=None:
                    nodo=Nodo(agente)
                    self.__comienzo=nodo
                    nodo.setSiguiente(aux)
                    self.__actual=nodo
                    self.__tope+=1
            else:
                i=1
                ant = aux
                aux = aux.getSiguiente()
                while i!=posicion:
                    i+=1
                    ant = aux
                    aux = aux.getSiguiente()
                if agente!=None:
                    nodo=Nodo(agente)
                    nodo.setSiguiente(aux)
                    ant.setSiguiente(nodo)
                    self.__tope+=1
        else:
            raise IndexError

    def agregarElemento(self,agente):
        if agente!=None:
            ant = self.__comienzo
            aux = ant.getSiguiente()
            while aux!=None:
                ant=aux
                aux=aux.getSiguiente()
            nodo=Nodo(agente)
            nodo.setSiguiente(aux)
            ant.setSiguiente(nodo)
            self.__tope+=1
        else:
            raise ValueError

    def TipoAgente(self,agente):
        if isinstance(agente, DocenteInvestigador):
            cadena = 'Docente Investigador'
        else:
            if isinstance(agente, Docente):
                cadena='Docente'
            else:
                if isinstance(agente, Investigador):
                    cadena = 'Investigador'
                else:
                    if isinstance(agente, Apoyo):
                        cadena = 'Personal de apoyo'
        return cadena

    def mostrarElemento(self,posicion):
        if posicion>=0 and posicion < self.__tope:
            aux=self.__comienzo
            i=0
            while i!=posicion:
                aux=aux.getSiguiente()
                i+=1
            print(self.TipoAgente(aux.getDato()))
        else:
            raise IndexError

    def Inciso4(self):
        newLista=[]
        catedra=str(input('Ingrese catedra: '))
        for dato in self:
            if isinstance(dato, DocenteInvestigador) and dato.getCatedra()==catedra:
                newLista.append(dato)
        newLista.sort(key=lambda agente: agente.getNom())
        for dato in newLista:
            print(dato.Info())

    def Inciso5(self):
        docInves=0
        investigadores=0
        area=str(input('Ingresar area: '))
        for dato in self:
            if isinstance(dato,Investigador) and dato.getArea()==area:
                investigadores+=1
                if isinstance(dato,DocenteInvestigador):
                    docInves+=1
        print('Investigadores: {}\nDocentes Investigadores: {}'.format(investigadores,docInves))

    def Inciso7(self):
        categoria=str(input('Ingrese categoria: '))
        importeExtra=0.0
        print('Nombre Apellido  Importe Docencia   Importe Investigacion')
        for dato in self:
            if isinstance(dato,DocenteInvestigador) and dato.getCatInvestigacion()==categoria:
                print('{}      ${:.2f}         ${:.2f}'.format(dato,dato.getImporteD(),dato.getImporteI()))
                importeExtra+=dato.getImporteD()+dato.getImporteI()
        print('Total de dinero en concepto de importe extra: ${:.2f}'.format(importeExtra))

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            Agentes=[personal.toJSON() for personal in self]
        )
        return d