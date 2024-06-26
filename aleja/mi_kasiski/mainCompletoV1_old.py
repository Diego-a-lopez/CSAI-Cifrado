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
    
# FASE 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_list(numbers):
    if len(numbers) == 0:
        return None  # If the list is empty, return None or handle the case appropriately
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

# FASE 5

def find_caesar_shift(substring):
    max_count = 0
    best_shift = 0
    
    for shift in range(26):
        shifted_text = ''.join(chr((ord(char) - 97 - shift) % 26 + 97) for char in substring.lower())
        count = sum(shifted_text.count(letter) for letter in 'etaoinshrdlu')
        
        if count > max_count:
            max_count = count
            best_shift = shift
    
    return best_shift

def generate_key(substrings):
    key = ''
    for substring in substrings:
        shift = find_caesar_shift(substring)
        key += chr((26 - shift) % 26 + 97)
    return key
   
# FASE 4

def create_substrings(text, key_length):
    substrings = [''] * key_length
    for i, char in enumerate(text):
        substrings[i % key_length] += char
    return substrings


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_del_archivo>")
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    texto_original = leer_archivo(nombre_archivo)
    texto_sin_espacios = texto_original.replace(" ", "").replace("\n", "")

    print("Longitud: "+str(len(texto_sin_espacios)))
    print("TIENE QUE DAR 404")
    
    subcadenas_repetidas = encontrar_subcadenas_repetidas(texto_sin_espacios)
    subcadenas_filtradas = filtrar_subcadenas(subcadenas_repetidas)
    
    todasdiferencias = []
    if subcadenas_filtradas:
        print("Subcadenas repetidas encontradas:")
        for subcadena in subcadenas_filtradas:
            print(subcadena)

            posiciones = encontrar_posiciones(texto_sin_espacios, subcadena)
            print("Posiciones:", posiciones)
            diferencias = calcular_diferencias(posiciones)
            print("Diferencias entre posiciones:", diferencias)
            
            for diferencia in diferencias:
                todasdiferencias.append(diferencia)  
              
             
    
    else:
        print("No se encontraron subcadenas repetidas.")
        
    print("Diferencias de las cadenas:", todasdiferencias)
        
    gcd_distances = gcd_of_list(todasdiferencias)
    print("Posible longitud de clave:", gcd_distances)

    quit()
    
    substrings = create_substrings(texto_sin_espacios, gcd_distances)
    print("Subcadenas creadas:")
    for i, substring in enumerate(substrings):
        print(f"Subcadena {i+1}: {substring}")
            
    key = generate_key(substrings)
    print("Posible clave encontrada:", key)
