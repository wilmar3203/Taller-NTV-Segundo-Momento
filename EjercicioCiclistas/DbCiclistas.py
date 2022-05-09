from Ciclista import Ciclista
class DbCiclistas:
      ciclistas =[]
      def Save(self,ciclista) -> list:
            if(type(ciclista) is dict):
                self.ciclistas.append(ciclista)
                return self.ciclistas
            return []

      def findAll(self)-> list:
            return self.ciclistas

      def findBy(self, tiempo)-> list:
        for ciclista in self.ciclistas:
            if(ciclista["tiempo"]==tiempo):
                return ciclista
        return []
