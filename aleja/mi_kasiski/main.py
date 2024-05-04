import sys
import os

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            texto = archivo.read()
            texto_sin_espacios_ni_saltos = texto.replace(" ", "").replace("\n", "")
            return texto_sin_espacios_ni_saltos
    except FileNotFoundError:
        return "El archivo no existe."






def encontrar_repeticiones(texto, longitud_min=3):
    repeticiones = {}
    for longitud in range(longitud_min, len(texto)):
        for i in range(len(texto) - longitud + 1):
            subcadena = texto[i:i+longitud]
            if subcadena in repeticiones:
                repeticiones[subcadena].append(i)
            else:
                repeticiones[subcadena] = [i]
    
    repeticiones_filtradas = {cadena: posiciones for cadena, posiciones in repeticiones.items() if len(posiciones) > 1}
    return repeticiones_filtradas






if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_del_archivo>")
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    texto_procesado = leer_archivo(nombre_archivo)
    print("Texto sin espacios ni saltos de línea:")
    print(texto_procesado)
    print("Tamaño: "+str(len(texto_procesado)))

    repeticiones = encontrar_repeticiones(texto_procesado)
    print("\nCadenas de caracteres que se repiten:")
    for cadena, posiciones in repeticiones.items():
        print(f"'{cadena}' se repite en las posiciones: {posiciones}")
