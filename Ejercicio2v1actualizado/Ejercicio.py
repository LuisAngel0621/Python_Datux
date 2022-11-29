## Ejercicio N°1
"""
print("\n")
print("Lista de números")
n = int(input("Ingrese la cantidad de números de la lista: "))
i = 0
numeros = []
aux = 0
verificacion = False
while i<n:
  aux = int(input("Ingrese un número: "))
  numeros.append(aux) 
  i=i+1
print("La lista es --> ",numeros)
print("...Verificación de múltiplos de 2")
for elemento in numeros:
  if elemento%2 == 0:
    verificacion = True
if verificacion == True:
  print("....Se encontró múltiplos de 2: ")
  for elemento in numeros:
    if elemento%2 == 0:
      print("\t Múltiplo de 2 --> ",elemento)
else:
  print("No hay múltiplos de 2 .........")
"""
## Ejercicio N°2
"""
print("\n")
print("Dibujo de Cuadrado -->")
print("")
lado = int(input('Ingrese el lado del cuadrado: '))
print("")
for i in range(lado):
  print('*'*(lado))
## Ejercicio N°3
"""
## Ejercicio N°3
"""
print("\n")
print("Dibujo de Triangulo -->")
print("")
h = int(input('Ingrese la altura del triangulo: '))
print("")
for f in range(h):
    print(' '*(h-f-1)+'*'*(2*f+1))
"""
## Ejercicio N°4
"""
print("\n")
print("Inserción de valores de 1 a 100 --> de 2 en 2")
listado = []
for elemento in range(1,100,2):
  listado.append(elemento)
print(listado)
"""
## Ejercicio N°5
"""
print("\n")
print("Función Multiplicativo de dos números")
def multiplicacion(num1,num2):
  return num1*num2
verificador = True
while verificador:
  numero1=int(input("Ingrese un primer número (> 0): "))
  if numero1 == 0:
    verificador = True
    print("\t Incorrecto... ")
  else:
    verificador = False
verificador = True
while verificador:
  numero2=int(input("Ingrese un segundo  número (> 0): "))
  if numero2 == 0:
    verificador = True
    print("\t Incorrecto... ")
  else:
    verificador = False
print("")
print("La multiplicación es: ",multiplicacion(numero1,numero2))
"""
## Ejercicio N°6
"""
print("\n")
print("Funciones")
print("¿Que desea realizar?")
print("1)saludar \n2)Realizar tarea \n3)Despedirse")
opcion = int(input("Escoga la opción --> "))
if opcion == 1 or opcion == 2 or opcion == 3:
  def saludar(nombre):
    print("Muy buenas ",nombre,"espero que tengas un buen día ¡Saludos!")
  def realizarTarea(tarea):
    print("La tarea de ",tarea,"ha sido realizado exitosamente..")
  def despedirse(nombre):
    print("Hasta luego",nombre,"espero que vuelva pronto")
  verificador = True
  while verificador:
    if opcion == 1:
      nombre = input("Ingrese su nombre: ")
      saludar(nombre)
      verificador = False
    elif opcion == 2:
      tarea = input("Ingrese su tarea: ")
      realizarTarea(tarea)
      verificador = False
    else:
      nombre = input("Ingrese su nombre: ")
      despedirse(nombre)
      verificador = False
else:
  print("La opción escogida es incorrecta..")
  print("\tSe cerrará el programa.....")  
"""
## Ejercicio N°7
"""
print("\n")
print("Función de mayor de dos números")
def mayor(num1,num2):
  if num1>num2:
    return num1
  elif num2>num1:
    return num2
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
print("El mayor número es --> ", mayor(numero1,numero2))
"""
## Ejercicio N°8
"""
import sys
def argumentos(*args):  --------------> OBSERVACIÓN
  print(*args)
argument = input("Ingrese argumentos: ")
argumentos(argument)
"""
## Ejercicio N°9
"""
print("\n")
print("")
numeros = [1,2,3,4,5]
def Lista(num):
  pos = 0
  for elemento in num:
    num[pos] = elemento+1
    pos = pos +1
  print(num)
Lista(numeros)
"""
## Ejercicio N°10
"""
print("\n")
print("Funcion String")
print("Menu de Funciones String")
print("Texto: ")
texto="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos ylos mezcló de tal manera que logró hacer un libro de textos especimen." 
print(texto)
print("1) Split \n2) Count \n3) Find \n4) uppercase \n5)lowecase")
opcion =int(input("Escoja la opción --> "))
if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
  def split(text):
    print(text.split(sep=" "))
  def count(text):
    print(text.count("Lorem"))
  def find(text):
    print(text.find("Ipsum"))
  def uppercase(text):
    print(text.upper())
  def lowecase(text):
    print(text.lower())        
  verificador = True
  while verificador:
    if opcion == 1:
      split(texto)
      verificador = False
    elif opcion == 2:
      count(texto)
      verificador = False
    elif opcion == 3:
      find(texto)
      verificador = False
    elif opcion == 4:
      uppercase(texto)
      verificador = False
    else:
      lowecase(texto)
      verificador = False
else:
  print("La opción escogida es incorrecta..")
  print("\tSe cerrará el programa.....")  
"""

## Ejercicio N°11
