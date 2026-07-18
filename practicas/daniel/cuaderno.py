import sqlite3

#*este comando sirve para establecer la conexion con la base de datos, si no existe la crea
#!conexion = sqlite3.connect("scans.db")

#*vale en la anterior estableci conexion con la lbreria para la base de datos
#*pero esto solo genera una conexion, ahora para poder darle ordenes necesito otra variable y otra funcion

#!ordenes = conexion.cursor() #*esta variable es la que me permite ejecutar ordenes en la base de datos

#*ahora voy a darle a la variable la funcion para ejecutar ordenes

#!ordenes.execute("CREATE TABLE IF NOT EXISTS historial(hash TEXT PRIMARY KEY, resultado TEXT)")
#!conexion.commit()
#!conexion.close()


def crear_base_de_datos():
    conexion = sqlite3.connect("scans.db")
    ordenes = conexion.cursor()
    ordenes.execute("CREATE TABLE IF NOT EXISTS historial(hash TEXT PRIMARY KEY, resultado TEXT)")
    conexion.commit()
    conexion.close()

crear_base_de_datos()
print("Base de datos y tabla 'historial' creadas correctamente.")

def crear_tabla_servidores():
    conexion = sqlite3.connect("scans.db")
    ordenes = conexion.cursor()
    ordenes.execute("CREATE TABLE IF NOT EXISTS servidores(hash TEXT PRIMARY KEY, canal_alertas TEXT)")
    conexion.commit()
    conexion.close()

crear_tabla_servidores()
print("Tabla 'servidores' creada correctamente.")