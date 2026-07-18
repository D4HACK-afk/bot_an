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

#*......................................................................................................../
def crear_base_de_datos():
    conexion = sqlite3.connect("scans.db")
    ordenes = conexion.cursor()
    ordenes.execute("CREATE TABLE IF NOT EXISTS historial(hash TEXT PRIMARY KEY, resultado TEXT)")
    conexion.commit()
    conexion.close()


crear_base_de_datos()
print("Base de datos y tabla 'historial' creadas correctamente.")
#*......................................................................................................../
def crear_tabla_servidores():
    conexion = sqlite3.connect("scans.db")
    ordenes = conexion.cursor()
    ordenes.execute("CREATE TABLE IF NOT EXISTS servidores(id_servidor TEXT PRIMARY KEY, canal_alertas TEXT)")
    conexion.commit()
    conexion.close()

crear_tabla_servidores()
print("Tabla 'servidores' creada correctamente.")
#*......................................................................................................../

def guardar_resultado(variable_hash, variable_resultado):
    conexion = sqlite3.connect("scans.db")
    ordenes = conexion.cursor()
    ordenes.execute("INSERT OR IGNORE INTO historial(hash, resultado) VALUES (?, ?)", (variable_hash, variable_resultado))
    conexion.commit()
    conexion.close()


guardar_resultado("abc123", "Resultado de ejemplo")
print("Resultado guardado correctamente en la tabla 'historial'.")
#*......................................................................................................../

def buscar_hash(variable_hash):
    conexion = sqlite3.connect("scans.db")
    ordenes = conexion.cursor()
    ordenes.execute("SELECT resultado FROM historial WHERE hash = ?", (variable_hash,))
    fila = ordenes.fetchone()
    conexion.close()
    return fila

registro = buscar_hash("abc123")
print("Resultado encontrado:", {registro})
#*......................................................................................................../