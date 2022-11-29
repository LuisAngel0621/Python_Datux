
##Clase Catálogo
class Catalogo:
    productos = []
    def __init__(self,productos = []):
        self.productos = productos

    def agregar(self, p):
        self.productos.append(p)

    def mostrar(self):
        for p in self.productos:
            print(p)

##Clase Producto
class Producto:
    def __init__(self,tipo,marca,precio):
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
    def __str__(self):
        return '{}({},{})'.format(self.tipo, self.marca,self.precio)


