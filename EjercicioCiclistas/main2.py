from Controller import Controller
ciclista = Controller()


nombre=input("ingrese nombre: ")
edad=int(input("ingrese edad: "))
pais=input("ingrese pais: ")
equipo=input("ingrese equipo: ")
tiempo=int(input("ingrese tiempo: "))
opcion = input("desea agregar otro ciclista? s/n:")
ciclista.ingresar(nombre,edad,pais,equipo,tiempo)  


while(opcion == 's'):
    nombre=input("ingrese nombre: ")
    edad=int(input("ingrese edad: "))
    pais=input("ingrese pais: ")
    equipo=input("ingrese equipo: ")
    tiempo=int(input("ingrese tiempo: "))
    opcion = input("desea agregar otro ciclista? s/n: ")
    ciclista.ingresar(nombre,edad,pais,equipo, tiempo)  

    

print(ciclista.all())