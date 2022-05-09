from DbCiclistas import DbCiclistas
from Ciclista import Ciclista
class Controller:
    def ingresar(self, nombre, edad, pais,equipo, tiempo):
        db = DbCiclistas()
        ciclista = Ciclista()
        ciclista.nombre=nombre
        ciclista.edad=edad
        ciclista.pais=pais
        ciclista.equipo=equipo
        ciclista.tiempo=tiempo
        registro_ciclista = dict(nombre=ciclista.nombre, edad=ciclista.edad, pais=ciclista.pais,equipo=ciclista.equipo,tiempo=ciclista.tiempo)
        if (db.Save(registro_ciclista)):
            return True
        return False
    def all (self)-> list:
            tiempo = []
            db = DbCiclistas()
            ciclistas= db.findAll()
            for ciclista in ciclistas:
                tiempo.append(ciclista["tiempo"])
            minimo = min(tiempo)
            return db.findBy(minimo)
    
