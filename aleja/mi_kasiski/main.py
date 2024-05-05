import sys
import os
from math import gcd

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            texto = archivo.read()
            texto = texto.replace(" ", "").replace("\n", "")
            return texto
    except FileNotFoundError:
        return "El archivo no existe."





def encontrar_subcadenas_repetidas(texto):
    subcadenas_repetidas = []
    n = len(texto)
    for longitud in range(3, n//2 + 1):
        for i in range(n - longitud + 1):
            subcadena = texto[i:i+longitud]
            veces_repetida = texto.count(subcadena)
            if veces_repetida > 1 and subcadena not in subcadenas_repetidas:
                subcadenas_repetidas.append(subcadena)
    subcadenas_filtradas = []
    for subcadena in subcadenas_repetidas:
        if all(len(subcadena) >= len(otra_subcadena) for otra_subcadena in subcadenas_repetidas if subcadena != otra_subcadena):
            subcadenas_filtradas.append(subcadena)
    return subcadenas_filtradas







def filtrar_subcadenas(subcadenas):
    subcadenas_filtradas = []
    for subcadena in subcadenas:
        es_subcadena = False
        for otra_subcadena in subcadenas:
            if subcadena != otra_subcadena and subcadena in otra_subcadena:
                es_subcadena = True
                break
        if not es_subcadena:
            subcadenas_filtradas.append(subcadena)
    return subcadenas_filtradas






if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_del_archivo>")
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    texto_procesado = leer_archivo(nombre_archivo)
    print("Texto sin espacios ni saltos de línea:")
    print(texto_procesado)
    
    subcadenas_repetidas = encontrar_subcadenas_repetidas(texto_procesado)
    subcadenas_filtradas = filtrar_subcadenas(subcadenas_repetidas)
    print(len("UÑE "))

    if subcadenas_filtradas:
        print("Subcadenas repetidas encontradas:")
        for subcadena in subcadenas_filtradas:
            print(subcadena)
            print("longitud: "+str(len(subcadena)))
            print()
    else:
        print("No se encontraron subcadenas repetidas.")
