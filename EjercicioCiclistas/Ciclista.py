
class Ciclista:
     __nombre = None
     __edad = None
     __pais = None 
     __equipo = None
     __tiempo = None


     @property
     def nombre(self):
         return self.__nombre

     @property
     def edad(self):
       return self.__edad

     @property
     def pais(self):
         return self.__pais

     @property
     def equipo(self):
         return self.__equipo

     @property
     def tiempo(self):
       return self.__tiempo
  

     @nombre.setter
     def nombre(self,nombre):
          self.__nombre=nombre
     
     @edad.setter
     def edad(self,edad):
         if(edad < 0):
             return False
         else:
            self.__edad=edad
    
     @pais.setter
     def pais(self,pais):
         self.__pais=pais

     @equipo.setter
     def equipo(self,equipo):
         self.__equipo=equipo
 
     @tiempo.setter
     def tiempo(self,tiempo):
         if(tiempo < 0):
             return False
         else:
            self.__tiempo=tiempo
       
