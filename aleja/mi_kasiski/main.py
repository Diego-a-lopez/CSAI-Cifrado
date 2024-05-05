import sys
import os
from math import gcd

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            return texto
    except FileNotFoundError:
        return "El archivo no existe."



# FASE 1

# Encuentra las cadenas repetidas
def encontrar_subcadenas_repetidas(texto):
    subcadenas_repetidas = []
    n = len(texto)
    for longitud in range(3, n//2 + 1):
        for i in range(n - longitud + 1):
            subcadena = texto[i:i+longitud]
            veces_repetida = texto.count(subcadena)
            if veces_repetida > 1 and subcadena not in subcadenas_repetidas:
                subcadenas_repetidas.append(subcadena.replace(" ", ""))
    return subcadenas_repetidas
    
    # Esto era si nos quisiesemos quedar con el más larg
    #subcadenas_filtradas = []
    #for subcadena in subcadenas_repetidas:
    #    if all(len(subcadena) >= len(otra_subcadena) for otra_subcadena in subcadenas_repetidas if subcadena != otra_subcadena):
    #        subcadenas_filtradas.append(subcadena)
    #return subcadenas_filtradas


# De las cadenas repetidas, si uno es subcadena de otro, se elimina de la lista
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


# FASE 2

def encontrar_posiciones(texto, subcadena):
    posiciones = []
    longitud_subcadena = len(subcadena)
    indice = 0
    while indice != -1:
        indice = texto.find(subcadena, indice)
        if indice != -1:
            posiciones.append(indice)
            indice += 1  # Avanzamos al siguiente carácter para evitar encontrar la misma subcadena en la misma posición
    return posiciones




def calcular_diferencias(posiciones):
    diferencias = []
    for i in range(len(posiciones) - 1):
        diferencia = posiciones[i + 1] - posiciones[i]
        diferencias.append(diferencia)
    return diferencias












if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_del_archivo>")
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    texto_original = leer_archivo(nombre_archivo)
    texto_sin_espacios = texto_original.replace(" ", "").replace("\n", "")
    #print("Texto sin espacios ni saltos de línea:")
    #print(texto_sin_espacios)


    print("Longitud: "+str(len(texto_sin_espacios)))
    print("TIENE QUE DAR 404")
    
    subcadenas_repetidas = encontrar_subcadenas_repetidas(texto_sin_espacios)
    subcadenas_filtradas = filtrar_subcadenas(subcadenas_repetidas)
    

    if subcadenas_filtradas:
        print("Subcadenas repetidas encontradas:")
        for subcadena in subcadenas_filtradas:
            print(subcadena)

            # Imprimir caracter a caracter
            #print("Caracteres:")
            #for caracter in subcadena:
            #    print(caracter+",")
            #    print("")  # Agregamos una línea en blanco después de imprimir cada subcadena
            #print("longitud: "+str(len(subcadena)))
            #print()

            posiciones = encontrar_posiciones(texto_sin_espacios, subcadena)
            #posiciones = encontrar_posiciones(texto_original, subcadena)
            print("Posiciones:", posiciones)
            diferencias = calcular_diferencias(posiciones)
            print("Diferencias entre posiciones:", diferencias)


            
    
    
    
    else:
        print("No se encontraron subcadenas repetidas.")
