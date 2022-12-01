import Paciente as Paciente
import Usuario as Usuario
import random
from os import system

print("")
print("\t\t!!!PROYECTO DATUX_PYTHON¡¡¡")
print("")
print("REGISTRO DE PACIENTES")
print("\t1)Iniciar Sesion \n\t2)Registro Usuario \n\t3)Salir")
opcion=int(input("Elige la opción: "))
verificador = True ##Variable que verifica si la opcion ha sido la correcta
while verificador:
    if(opcion == 1):
        system("cls")
        print("INICIO DE SESION")
        usuario = input("Username: ")
        contra = input("Contraseña: ")
        validacion = Usuario.usuario.readRowInsertUsuario(usuario,contra)
        if len(validacion) != 0:## Revisarrrrrrr ojoooooo GAAAAAAAAAAAAAAAAAAAAAA
            verificador = False
            verificador2 = True
            while verificador2:
                system("cls")
                print("Bienvenido,",usuario)
                print("")
                print("\t\tREGISTRO DE PACIENTES")
                print("Menú de Opciones")
                print("\t1)Registrar Paciente \n\t2)Visualizar Pacientes \n\t3)Cerrando Sesión")
                opcion2=int(input("Elige la opción: "))
                verificador3 = True ##Variable que verifica si la opcion ha sido la correcta
                while verificador3:
                    pregunta = "No"
                    if(opcion2 == 1):
                        system("cls")
                        nombre=input("Nombres: ")
                        appaterno=input("Apellido Paterno: ")
                        apmaterno=input("Apellido Materno: ")
                        ciudad=input("Ciudad: ")
                        direccion=input("Direccion: ")
                        numhogar=int(input("Telefono del Hogar: "))
                        nummovil=int(input("Telefono Móvil: "))
                        fechanac=input("Fecha de Nacimiento (dd/mm/yyyy): ")
                        sexo=input("Sexo (M/F): ")
                        gruposangui=input("Grupo Sanguineo: ")
                        print("")
                        Paciente.paciente(nombre,appaterno,apmaterno,ciudad,direccion,numhogar,nummovil,fechanac,sexo,gruposangui)
                        Paciente.paciente.insertRowPaciente(nombre,appaterno,apmaterno,ciudad,direccion,numhogar,nummovil,fechanac,sexo,gruposangui)
                        Paciente.paciente.readRowInsertPaciente(nombre)
                        print("¿Desea seguir insertando?")
                        pregunta = input("(Si/No) --> ")
                        if pregunta.upper() == "SI":
                            verificador3 = True
                        else:
                            verificador3 = False
                            print("¿Desea retrocer al menu de opciones?")
                            pregunta = input("(Si/No) --> ")
                        

                    elif(opcion2 == 2):
                        system("cls")
                        print("Pacientes Registrados: ")
                        Paciente.paciente.readRow()
                        print("¿Desea retrocer al menu de opciones?")
                        pregunta = input("(Si/No) --> ")
                        verificador3=False

                    elif(opcion2 == 3):
                        system("cls")
                        print("Cerrando Sesión... ")
                        pregunta = "No"
                        verificador3=False                    
                    else:
                        print("La opción escogida es inválida !!!!")
                        pregunta = input("Desea escoger de nuevo una opción (Si/No) --> ")
                        verificador3 = False
                    
                    if pregunta.upper() == "SI":
                        verificador2=True
                    else:
                        verificador2=False
                        print("¡Cerrando el programa!")
                        print("Hasta luego, ",usuario,"!!!")
        else:
            print("Usuario incorrecto ....")
            print("Se regresará al inicio de sesion ->")
            input("Aplaste el teclado (enter) -->")
            verificador=True
        
    elif(opcion == 2):
        system("cls")
        print("REGISTRO DE USUARIO")
        usuario = input("Username: ")
        contra = random.randint(1000,9999)
        print("Contraseña: ",contra)
        dni = int(input("DNI: "))
        celular = int(input("Celular: "))
        Usuario.usuario.insertRowUsuario(usuario,contra,dni,celular)
        print("Inicio Sesion con la cuenta creada ....")
        print("¡Anote su username y su contraseña antes de iniciar sesion!")
        input("Si ya anoto dale (enter) -->")
        opcion=1
        verificador=True
    
    elif(opcion == 3):
        system("cls")
        print("Saliendo del Programa.......")
        verificador=False
    
    else:
        print("La opción escogida es inválida !!!!")
        pregunta = input("Desea escoger de nuevo una opción (Si/No) --> ")
        if pregunta.upper() == "SI":
            verificador = True
        else:
            verificador = False