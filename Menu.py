import os
from Lista import ListaAgentes
from ObjectEncoder import ObjectEncoder

class Menu(object):
    __switcher=None
    __jsonF=ObjectEncoder()
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.opcion7,
                            8:self.opcion8
                            }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,lista):
        try:
            func=self.__switcher.get(op)
            func(lista)
        except TypeError:
            print("Opción no válida")
    def salir(self):
        print('Salir')
    def opcion1(self,lista):
        posicion = int(input('Ingresar posicion: '))
        os.system('cls')
        try:
            agente = lista.crear()
            try:
                lista.insertarElemento(posicion - 1, agente)
            except IndexError:
                print('Posicion incorrecta')
        except ValueError:
            print('Estado incorrecto')

    def opcion2(self,lista):
        try:
            agente = lista.crear()
            lista.agregarElemento(agente)
        except ValueError:
            print('Estado incorrecto')

    def opcion3(self,lista):
        posicion = int(input('Ingresar posicion: '))
        os.system('cls')
        try:
            lista.mostrarElemento(posicion - 1)
        except IndexError:
            print('Posicion incorrecta')

    def opcion4(self,lista):
        lista.Inciso4()

    def opcion5(self,lista):
        lista.Inciso5()

    def opcion6(self,lista):
        print('Tipo Agente  Nombre   Apellido    Sueldo')
        for dato in lista:
            print('{} {} ${:.2f}'.format(lista.TipoAgente(dato),dato,dato.getSueldo()))

    def opcion7(self,lista):
        lista.Inciso7()

    def opcion8(self,lista):
        d = lista.toJSON()
        self.__jsonF.guardarJSONArchivo(d, 'personal.json')
        print('Datos guardados')
