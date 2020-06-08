import os
from Lista import ListaAgentes
from Menu import Menu
from ObjectEncoder import ObjectEncoder

if __name__ == '__main__':

    lista=ListaAgentes()
    jsonF = ObjectEncoder()
    diccionario = jsonF.leerJSONArchivo('personal.json')
    lista = jsonF.decodificarDiccionario(diccionario)
    menu = Menu()
    salir = False

    while not salir:
        print('\nMenú de Opciones:\n--------------------------')
        print("1. Insertar a agentes a la colección")
        print("2. Agregar agentes a la colección")
        print("3. Mostrar tipo de agente de una posicion")
        print("4. Listado de agentes que se desempeñan como docentes investigadores en una catedra")
        print("5. Cantidad de agentes que son docente investigador "
              "y cantidad de investigadores que trabajan en un área")
        print("6. Mostrar agentes")
        print("7. Listado de agentes de una categoria de investigacion")
        print("8. Guardar datos")
        print("0. Salir")
        try:
            op = int(input('Ingresar una opcion: '))
            os.system('cls')
            menu.opcion(op, lista)
            salir = op == 0
        except ValueError:
            print("Opción no válida")


