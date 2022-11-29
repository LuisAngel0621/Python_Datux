## LISTA DE EJERCCIOS ##

## Ejercicio N°1 
"""
print("\n")
print("Ingrese sus datos personales: ")
print("")
Nombre = input("Nombre: ")
Apellido = input("Apellido: ")
Nacionalidad = input("Nacionalidad: ")
Ciudad = input("Ciudad: ")
Domicilio = input("Domicilio: ")
Profesion = input("Profesion: ")
Telefono = int(input("Telefono: "))
Correo = input("Correo Electronico: ")
Fecha = input("Fecha Nacimiento: ")
dni = int(input("DNI: "))

print("\n")
print("DATOS PERSONALES")
print("")
print("\tNombre: \t",Nombre)
print("\tApellido: \t",Apellido)
print("\tNacionalidad: \t",Nacionalidad)
print("\tCiudad: \t",Ciudad)
print("\tDomicilio: \t",Domicilio)
print("\tProfesion: \t",Profesion)
print("\tTelefono: \t",Telefono)
print("\tCorreo: \t",Correo)
print("\tF. Nacimiento: \t",Fecha)
print("\tDNI: \t\t",dni)
print("")
"""

## Ejercicio N°2
"""
import math
pi=math.pi
print("\n")
print("Cálculo de área de un círculo")
Radio = float(input("\tIngrese el valor del radio: "))
Area = pi*Radio*Radio
print("\tÁrea del Círculo: ", Area)
print("")
"""

## Ejercicio N°3
"""
print("\n")
print("Operaciones matemáticas básicas")
print("")
Num1 = float(input("Ingrese el primer número: "))
Num2 = float(input("Ingrese el segundo número: "))
Num3 = float(input("Ingrese el tercer número: "))
print("\n")
print("Suma")
Suma = Num1 + Num2 + Num3
print("\tLa suma de los tres números es: ",Suma)
print("")
print("Resta")
Resta = Num1 - Num2 - Num3
print("\tLa resta de los tres números es: ",Resta)
print("")
print("Multiplicación")
Multiplicacion = Num1 * Num2 * Num3
print("\tLa multiplicación de los tres números es: ",Multiplicacion)
print("")
"""

## Ejercicio N°4
"""
import re
print("\n")
print("Tipos de Datos")
variable = input('Ingrese un valor: ')

if(not re.search("^[0-9]+.?[0-9]+$",variable)):
    print("Es una cadena", type("Cadena"))
elif(re.search("\.",variable)):
    print("Es una flotante", type(12.3))
else:
    print("Es un entero", type(14))
"""

## Ejercicio N°5

## Ejercicio N°6
"""
print("\n")
print("Suma de números consecutivos")
variable = int(input("Ingrese un número: "))
suma = 0
varaux = 1
while (varaux <= variable):
    suma = suma + varaux
    varaux = varaux + 1 
for i in range(variable):
    print(i+1,end = "")
    if i <= variable-2:
        print(" + ", end="")
print("\n La suma de los numeros es: ",suma)
"""

## Ejercicio N°7
"""
print("\n")
print("Lectura de dos números")
Numero1 = int(input("Ingrese un primer número: "))
Numero2 = int(input("Ingrese un segundo número: "))
if Numero1 == Numero2:
    print("\tLos números ingresados son iguales --> ", Numero1, " = ", Numero2)
if Numero1 != Numero2:
    print("\tLos números ingresados son diferentes --> ", Numero1, " != ", Numero2)
if Numero1 > Numero2:
    print("\tEl primer número es mayor que el segundo --> ", Numero1, " > ", Numero2)
if Numero2 >= Numero1:
    print("\tEl segundo número es mayor o igual que el primero --> ", Numero2, " >= ", Numero1)
"""

## Ejercicio N°8
"""
print("\n")
print("!Verificación de Contraseña¡")
print("")
codigo = "contraseña"
verificación = True
while verificación:
    contraseña = input("\nIngrese la contraseña: ")
    if contraseña.upper() == codigo.upper():
        print("\tLa contraseña ingresada es la correcta!!!!")
        verificación = False
    else:
        print("\tLa contraseña ingresada es incorrecta uu. Ingrese devuelta la contraseña!!!")
        verificación = True
"""

## Ejercicio N°9
"""
print("\n")
print("Tipo de número entero")
print("")
verificación = True
while verificación:
    print("")
    Num1 = int(input("Digite un número entero: "))    
    if Num1%2 == 0:
        print("\tEl dígito ingresado es par --> múltiplo de 2")
        verificación = False
    else:
        print("\tEl dígito ingresado es impar --> es diferente a múltiplo de 2")
        pregunta = input("¿Desea ingresar otro número? Si/No: ")
        if pregunta.upper() == "SI":
            verificación = True
        else:
            verificación = False
"""

## Ejercicio N°10
"""
print("\n")
print("Programa de Cálculo de Penalidad por Mora")
Deuda = float(input("Ingrese el monto de la deuda: "))
Mora = int(input("Ingrese los días de demora: "))
Penalidad = 0.0
if Mora >=1 and Mora <=10:
    Penalidad = Deuda*0.05
    print("La penalidad a pagar es de: ", Penalidad)
elif Mora >10 and Mora <=30:
    Penalidad = Deuda*0.08
    print("La penalidad a pagar es de: ", Penalidad)
else:
    Penalidad = Deuda*0.10
    print("La penalidad a pagar es de: ", Penalidad)
"""

## Ejercicio N°11
"""
print("\n")
print("Programa de Operaciones con dos números")
print("")
PrimerNumero = int(input("Ingrese el primer número: "))
SegundoNumero = int(input("Ingrese el segundo número: "))
verificacion = True
while verificacion:
    print("")
    print("Menú de Opciones: ")
    print("1) Mostrar una suma de los dos números \n2) Mostrar una resta de los dos números \n3) Mostrar una multiplicación de los dos números")
    opcion = int(input("Escoga una opción --> "))
    if opcion == 1:
        suma = PrimerNumero + SegundoNumero
        print("La suma de los dos números es: ", suma)
        verificacion = False
    elif opcion == 2:
        resta = PrimerNumero - SegundoNumero
        print("La resta de los dos números es: ", resta)
        verificacion = False        
    elif opcion == 3:
        multiplicacion = PrimerNumero * SegundoNumero
        print("La multiplicación de dos números es: ", multiplicacion)
        verificacion = False
    else:
        print("La opción escogida es inválida !!!!")
        pregunta = input("Desea escoger de nuevo una opción (Si/No) --> ")
        if pregunta.upper() == "SI":
            verificacion = True
        else:
            verificacion = False
"""

## Ejercicio N°12
"""
print("\n")
print("Programa de verificación de vocales")
letra = input("Ingrese una letra: ").lower()
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Es vocal --> ", letra)
else:
    if len(letra) == 1:
        print("Es una consonante --> ", letra)
    else:
        print("No se puede procesar el dato")
"""

## Ejercicio N°13
"""
print("\n")
print("Lista de Estudiantes")
estudiantes = ["Juancito Perez Gonzales", "Roberto Gutierrez Apaza", "Gilberto Muñoz Ayala", "Richard Quispe Huaman", "Alfonso Haynate Flores"]
print("La lista está conformado por: ", estudiantes)
print("El tamaño de la lista es de : ",len(estudiantes))
print("El último elemento de la lista es: ",estudiantes[-1])
estudiantes.reverse()
print("El orden inverso: ", estudiantes)
"""

## Ejercicio N°14
"""
print("\n")
print("Definición de un Diccionario")
diccionario = {
    'Estudiantes':(
        'Luis Quispe Ascues',
        'Hermilindo Acuña Flores',
        'Jose Hermalinio Zapata',
        'Jorge Perez Godoy',
    ),
    'Colegios':[
        'San Gerardo',
        'San Felipe',
        'Colegio Ingenieros',
        'Juventud Cientifica'
    ]
}

print("Indique que posición desea modificar del último elemento [0-3]: ")
print("Colegios --> ", diccionario["Colegios"])
posicion = int(input("Posición -->"))
nuevo = input("\t" + diccionario['Colegios'][posicion] + "--> ")
diccionario['Colegios'][posicion] = nuevo
print("Colegio actualizado --> ",diccionario['Colegios'])
"""

## Ejercicio N°15
"""
print("\n")
print("Bienvenido a un Menú Iteractivo")
verificador = True
print("A continuación se presentará las siguientes opciones a escoger....")
while verificador:
    print("")
    print("1) Saludar \n2) Multiplicación de dos números \n3) Salir")
    opcion = input("Ingrese la opción --> ")
    if opcion == '1':
        print("Muy buenas, me hes grato saludarle y desearle un hermoso día")
        verificador=False
    elif opcion == '2':
        Numero1 = int(input("Ingrese un primer numero: "))
        Numero2 = int(input("Ingrese un segundo número: "))
        multiplicacion = Numero1 * Numero2
        print("La mulitiplicación de los números ingresados es: ", multiplicacion)
        verificador=False
    elif opcion == '3':
        print("Muchas gracias por su visita a este programa, vuelva pronto !!! :D ")
        verificador=False
    else:
        print("Opción inválida, porfavor vuelva a ingresar una opción -->")
        verificador = True
"""

## Ejercicio N°16
"""
print("\n")
print("Lista de Personas que tienen mayor de edad:")
elementos = [['Luis',20],['Marco',18],['Sandro',14],['Kenia',16],['Mendez',32],['Piero',22]]
iterador = 0
limite = len(elementos)
while iterador < limite:
    if elementos[iterador][1]>=18:
        print("\t",elementos[iterador])
    iterador = iterador + 1
"""
