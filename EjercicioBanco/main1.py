# Importando la clase Banco
from Banco.Banco import Banco

banco = Banco()

banco.saldo = 2000000

banco.nombre = input("Digite su nombre apreciado cliente: ")
banco.apellido = input("Digite su apellido: ")
banco.cedula = input("Digite su numero de cedula: ")
banco.ciudad = input("Digite la ciudad de residencia: ")
banco.numeroCuenta = input("Digite su numero de cuenta: ")
print("")
print("---------------------------------------------------")

print("DATOS DEL CLIENTE")
print("---------------------------------------------------")
print("")
print(f"Nombre completo: {banco.nombre} {banco.apellido}")
print(f"Documento Nº: {banco.cedula}")
print(f"Ciudad de residencia: {banco.ciudad}")
print(f"Numero de la cuenta: {banco.numeroCuenta}")
print("---------------------------------------------------")

banco.consultarSaldo()
banco.consignarSaldo(400000)
banco.consultarSaldo()
banco.retirar(100000)
banco.consultarSaldo()

