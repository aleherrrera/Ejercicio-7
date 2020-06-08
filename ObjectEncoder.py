import json
from pathlib import Path
from Lista import ListaAgentes
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from Apoyo import Apoyo

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ListaAgentes':
                agentes=d['Agentes']
                dAgentes = agentes[0]
                lista=class_()
                for i in range(len(agentes)):
                    dAgentes=agentes[i]
                    class_name=dAgentes.pop('__class__')
                    class_=eval(class_name)
                    atributos=dAgentes['__atributos__']
                    unAgente=class_(**atributos)
                    lista.cargar(unAgente)
        return lista

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario