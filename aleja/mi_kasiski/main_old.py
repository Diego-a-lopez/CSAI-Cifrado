import sys
import os
from math import gcd

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            texto_sin_espacios_ni_saltos = texto.replace(" ", "").replace("\n", "")
            return texto_sin_espacios_ni_saltos
    except FileNotFoundError:
        return "El archivo no existe."

def encontrar_repeticiones(texto, longitud_min=3):
    repeticiones = {}
    for longitud in range(len(texto), longitud_min - 1, -1):
        for i in range(len(texto) - longitud + 1):
            subcadena = texto[i:i+longitud]
            if subcadena in texto[i+1:]:
                if subcadena in repeticiones:
                    if len(subcadena) > len(repeticiones[subcadena]):
                        repeticiones[subcadena] = subcadena
                else:
                    repeticiones[subcadena] = subcadena
    
    return repeticiones


def filtrar_subcadenas(repeticiones):
    repeticiones_filtradas = repeticiones.copy()
    for cadena1 in repeticiones:
        for cadena2 in repeticiones:
            if cadena1 != cadena2 and cadena1 in cadena2:
                del repeticiones_filtradas[cadena1]
                break
    return repeticiones_filtradas




def quedarse_con_mas_largas(repeticiones):
    repeticiones_filtradas = {}
    for cadena, repeticion in repeticiones.items():
        if cadena not in repeticiones_filtradas:
            repeticiones_filtradas[cadena] = repeticion
        else:
            if len(repeticion) > len(repeticiones_filtradas[cadena]):
                repeticiones_filtradas[cadena] = repeticion
    
    print(repeticiones_filtradas)
    #quit()
    return repeticiones_filtradas





def calcular_distancias(repeticiones):
    distancias = {}
    for cadena in repeticiones.values():
        posiciones = [i for i, letra in enumerate(texto_procesado) if texto_procesado.startswith(cadena, i)]
        distancias[cadena] = [posiciones[i+1] - posiciones[i] for i in range(len(posiciones)-1)]
    return distancias





def encontrar_maximo_comun_divisor(diccionario):
    """
    Método para calcular el máximo común divisor (MCD) de los números en un diccionario de listas.
    Utiliza la función gcd de la biblioteca math.
    """
    # Extraer todos los números del diccionario
    numeros = []
    for lista in diccionario.values():
        numeros.extend(lista)

    # Calcular el MCD utilizando la función gcd de la biblioteca math
    mcd = numeros[0]
    for num in numeros[1:]:
        mcd = gcd(mcd, num)

    return mcd












if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_del_archivo>")
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    texto_procesado = leer_archivo(nombre_archivo)
    #print("Texto sin espacios ni saltos de línea:")
    #print(texto_procesado)

    repeticiones = encontrar_repeticiones(texto_procesado)

    

    repeticiones_filtradas = filtrar_subcadenas(repeticiones)

    print(repeticiones_filtradas)

    
    repeticiones_mas_largas = quedarse_con_mas_largas(repeticiones_filtradas)

    print("\nCadenas de caracteres que se repiten:")
    for repeticion in repeticiones_mas_largas.values():
        print(f"'{repeticion}' se repite")

    
    distancias = calcular_distancias(repeticiones_mas_largas)
    print("\nDistancias entre repeticiones:")
    for cadena, lista_distancias in distancias.items():
        print(f"'{cadena}': {lista_distancias}")

    #print(distancias)
    
    mcd_encontrado = encontrar_maximo_comun_divisor(distancias)
    print("\nFactores comunes de las distancias:")
    print(mcd_encontrado)
