import sqlite3
import hashlib
import os
#!generador de hashes para los archivos subidos

def calcular_hash(ruta_archivo): 
    with open (ruta_archivo, "rb") as archivo: #*pasar el archivo a binario para poder calcular el hash
        contenido = archivo.read()             #* almacenar el contenido binario a una variable 
        generador = hashlib.sha256()           #* crear una variable que almacena la funcion de hash sha256
        generador.update(contenido)            #*actualizar el generador con el contenido del archivo
        hash_final = generador.hexdigest()     #* obtener el hash final en formato hexadecimal(texto plano y numeros)
#! condicional para detectar si el hash es igual al hash de un archivo malicioso conocido, si es asi se devuelve un mensaje de advertencia, si no se devuelve el hash final
        hash_maligno = "1bf9d267dfeb48e42b64181ceb7e76944297ddc1bb6a0261323faff7e0ee6117"
    if hash_final == hash_maligno:
        return "este archivo te podria romper el pc, es un archivo malicioso, por eso no te dare el hash"    
    else: 
       return hash_final
    
ola = calcular_hash("hollow.jpg")
print(f"El hash del archivo es: {ola}")