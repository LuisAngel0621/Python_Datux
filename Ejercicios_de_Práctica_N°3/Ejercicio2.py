
class Animal:
    def __init__(self,tipo,raza, ojos, altura,nombre):
        self.tipo = tipo
        self.raza = raza
        self.ojos = ojos
        self.altura = altura
        self.nombre = nombre
        print("Raza: ",raza,"\nOjos: ",ojos,"\nAltura: ",altura)    
    def __str__(self):
        return '{} - {}'.format(self.tipo,self.nombre)


class Perro(Animal):

    def sonido(self):    
        print("Ladra")    

class Gato(Animal):
    
    def sonido(self):    
        print("Maulla")        

