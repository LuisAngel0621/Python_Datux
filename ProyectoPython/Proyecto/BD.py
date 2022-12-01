import sqlite3 as sql

##Creacion de la base de datos
def createBD():
    try:
        conn = sql.connect("BaseDatos.sqlite3")
        conn.commit()##Guardar los cambios realizados
        conn.close()##Cierre de la BD
    except:
        print("Error.....")

##Creacion de la tabla PACIENTES
def createTable():
    try:
        conn = sql.connect("BaseDatos.sqlite3")
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE PACIENTES(
                nombre          text,
                appaterno       text,
                apmaterno       text,
                ciudad          text,
                direccion       text,
                numhogar        integer,
                nummovil        integer,
                fechanacim      text,
                sexo            text,
                gruposangui     text
            )
            """
        )
        conn.commit()##Guardar los cambios realizados
        conn.close()##Cierre de la BD
    except:
        print("Error....")

def createTable2():
    try:
        conn = sql.connect("BaseDatos.sqlite3")
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE USUARIO(
                username        text,
                contraseña      text,
                dni             integer,
                celular         integer
            )
            """
        )
        conn.commit()##Guardar los cambios realizados
        conn.close()##Cierre de la BD
    except:
        print("Error....")

##Clase de Función insertar y lectura en la BD
class funcionesPaciente:

    ##Funcion Insertar datos Paciente
    def insertRowPaciente(nombre,appaterno,apmaterno,ciudad,direccion,numhogar,nummovil,fechanac,sexo,gruposangui):
        try:
            conn = sql.connect("BaseDatos.sqlite3")
            cursor = conn.cursor()
            instruccion = f"INSERT INTO PACIENTES VALUES('{nombre}','{appaterno}','{apmaterno}','{ciudad}','{direccion}',{numhogar},{nummovil},'{fechanac}','{sexo}','{gruposangui}')"
            cursor.execute(instruccion)
            conn.commit()##Guardar los cambios realizados
            conn.close()##Cierre de la BD
        except:
            print("Error...")

    ##Funcion de Visualizar data
    def readRow():
        try:
            conn = sql.connect("BaseDatos.sqlite3")
            cursor = conn.cursor()
            instruccion = f"SELECT * FROM PACIENTES"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            conn.commit()##Guardar los cambios realizados
            conn.close()##Cierre de la BD
            for e in datos:
                print(e)

        except:
            print("Error.....")
    
    ##Funcion de Visualizar data por cada inserte que se realiza
    def readRowInsertPaciente(nombre):
        try:
            conn = sql.connect("BaseDatos.sqlite3")
            cursor = conn.cursor()
            instruccion = f"SELECT * FROM PACIENTES WHERE nombre = '{nombre}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            conn.commit()##Guardar los cambios realizados
            conn.close()##Cierre de la BD
            print(datos)
            print("El registro se ha realizado satisfactoriamente ...")
        except:
            print("Error.....")


class funcionesUsuario:

    ##Funcion Insertar datos Usuario
    def insertRowUsuario(username,contra,dni,celular):
        try:
            conn = sql.connect("BaseDatos.sqlite3")
            cursor = conn.cursor()
            instruccion = f"INSERT INTO USUARIO VALUES('{username}','{contra}',{dni},{celular})"
            cursor.execute(instruccion)
            conn.commit()##Guardar los cambios realizados
            conn.close()##Cierre de la BD
        except:
            print("Error...")

    ##Funcion de validacion de usuario
    def readRowInsertUsuario(username,contra):
        try:
            conn = sql.connect("BaseDatos.sqlite3")
            cursor = conn.cursor()
            instruccion = f"SELECT * FROM USUARIO WHERE username = '{username}' and contraseña = '{contra}'"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            conn.commit()##Guardar los cambios realizados
            conn.close()##Cierre de la BD
            return datos
        except:
            return datos
##Permite la creación de la BD y la tabla solo se ejecuta una vez
if __name__ == "__main__":
    funcionesUsuario.insertRowUsuario("Luis0921","7485","4756812","941236475")