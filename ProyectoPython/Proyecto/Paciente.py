from BD import funcionesPaciente

##Clase de Paciente
class paciente(funcionesPaciente):
    def __init__(self,nombres,appaterno,apmaterno,ciudad,direccion,numhogar,nummovil,fechanacim,sexo,gruposangui):
        self.nombres=nombres
        self.appaterno = appaterno
        self.apmaterno=apmaterno
        self.ciudad=ciudad
        self.direccion=direccion
        self.numhogar=numhogar
        self.nummovil=nummovil
        self.fechanacim=fechanacim
        self.sexo = sexo       
        self.gruposangui = gruposangui
        print("Registro en proceso....")

