class Banco:
    def __init__(self):
        self.__nombre=None
        self.__apellido=None
        self.__cedula=None
        self.__ciudad=None
        self.__numeroCuenta=None
        self.__saldo=None

    
    # Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def cedula(self):
        return self.__cedula

    @property
    def ciudad(self):
        return self.__ciudad

    @property
    def numeroCuenta(self):
        return self.__numeroCuenta

    @property
    def saldo(self):
        return self.__saldo      


    # Setters
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre     

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido=apellido    

    @cedula.setter
    def cedula(self,cedula):
        self.__cedula=cedula  

    @ciudad.setter
    def ciudad(self,ciudad):
        self.__ciudad=ciudad

    @numeroCuenta.setter
    def numeroCuenta(self,numeroCuenta):
        self.__numeroCuenta=numeroCuenta 

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo=saldo  


    # Métodos

    def consultarSaldo(self):
        print(f"Su saldo actual es de ${self.saldo}")

    def consignarSaldo(self, consignado):
        self.saldo = self.saldo + consignado
        print(f"Consignación éxitosa")

    def retirar(self, retiro):
        self.saldo = self.saldo - retiro
        print("Retiro éxitoso")
