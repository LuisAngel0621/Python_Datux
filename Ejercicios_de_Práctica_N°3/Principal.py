##Ejercicio N°1
import Ejecicio1 as ejerc
import Ejercicio2 as ejerc1
import os
import random
##import requests


##LLamado de objeto de ejercicio N°1
'''
Product = ejerc.Producto("Llanta","Toyota",120)
Cata = ejerc.Catalogo([Product])
Cata.mostrar()
'''

##LLamado de objeto de ejercicio N°2
'''
Perrito = ejerc1.Perro("Canino","Chiwawa","marrones","bajo","Betito")
Perrito.sonido()
print("")
Gatito = ejerc1.Gato("Felino","Persa","verdes","mediano","Garfy")
Gatito.sonido()
'''

##Ejericio N°3
'''
print(os.getcwd())
os.listdir('./Principal')
os.environ()
'''
##Ejericio N°5
'''
print("")
print("Núnmeros Aleatorios del 1 al 100")
print("Desea números enteros o reales?")
opcion = int(input("1)Entero \n2)Real \nOpcion --> "))
if opcion == 1:
    print(random.randint(1,100))
else:
    print(random.uniform(1,100))
'''

##Ejercicio N°6

'''
url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat

# https://apis.net.pe/api-tipo-cambio.html

# 1. conectarme al sitio
response = requests.get(url)

response.json() # nos brinda la información en formato JSON
# 2. Recupero la informacion como json
res=response.json()

# obteniendo tipo cambio

# 3. Recupero valor tipo cambio - compra - venta
dolar_compra = res['compra']
dolar_venta = res['venta']

print("Consultas sobre compra y venta del dolar $: ")
print("Seleccione la consulta que desea realizar")
opcion = int(input("1)Compra de Dolar \n2)Venta de Dolar \nOpcion --> "))
if opcion == 1:
    print(dolar_compra)
else:
    print(dolar_venta)
'''

##Ejercicio N°8
'''
texto = " “Python es uno de los lenguajes deprogramación dinámicos más populares que existen entre los que se encuentran Java,Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje 'scripting', es realmente un lenguaje de propósito general. En la actualidad, Python es usado para todo, desde simples 'scripts', hasta grandes servidores web que proveen servicio ininterrumpido 24×7. Es utilizado para la programación de interfaces gráficas y bases de datos, programación web tanto en el cliente como en el servidor (véase Django o Flask) y 'testing' de aplicaciones”."
print("TEXTO:")
print(texto)
validacion = int(texto.find("Python"))
if validacion != -1 :
    print("La palabra python existe!!")
else:
    print("La palabra python no existe....")
'''

## Ejercicio N°9
'''
print("")
texto = " “Python es uno de los lenguajes deprogramación dinámicos más populares que existen entre los que se encuentran Java,Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje 'scripting', es realmente un lenguaje de propósito general. En la actualidad, Python es usado para todo, desde simples 'scripts', hasta grandes servidores web que proveen servicio ininterrumpido 24×7. Es utilizado para la programación de interfaces gráficas y bases de datos, programación web tanto en el cliente como en el servidor (véase Django o Flask) y 'testing' de aplicaciones”."
print("TEXTO:")
print(texto)
conteo = texto.count("Python")
print("")
print("\tLa cantidad de repeticiones de la palabra Python es de: ",conteo)
'''