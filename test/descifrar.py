import sys
import os

# Entradas
english_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
spanish_chars = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
#french_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            return texto
    except FileNotFoundError:
        return "El archivo no existe."
    except EOFError:
        print("Error: EOF reached unexpectedly.")
        return None

# Otener numero de posicion
def charToNumber(letra, idioma):
    # Convertir la letra y la cadena a mayúsculas para hacer la búsqueda insensible a mayúsculas y minúsculas
    letra = letra.upper()
    idioma = idioma.upper()

    # Iterar sobre la cadena para buscar la letra
    for numero in range(len(idioma)):
        if idioma[numero] == letra:
            return numero  # Devolver la posición si se encuentra la letra
    # Si la letra no se encuentra, devolver -1 o algún otro valor por defecto
    return -1



def numberToChar(numero, idioma):
    return idioma[numero]

# Cifrado Vigenere
def descifrado_vigenere(inpuTXT, clave, idioma):
    
    texto_cifrado = "" # Texto de salida
    clave_repetida = "" # Clave que luego se generara a partir de kasiski

    # Eliminacion de espacios
    inpuTXT = inpuTXT.replace(" ", "")

    # Convertir entradas a mayúsculas
    inpuTXT = inpuTXT.upper()
    clave = clave.upper()
    
    for i in range(len(inpuTXT)):
        clave_repetida += clave[i % len(clave)]
        
    for i in range(len(inpuTXT)):

        # Obtenemos las posiciones de las letras
        pos_char_texto = charToNumber(inpuTXT[i], idioma)
        pos_char_clave = charToNumber(clave_repetida[i], idioma)
        
        # Desifrado Vigenère ==> Ci= (Mi-Ki) mod N
        texto_cifrado += numberToChar((pos_char_texto - pos_char_clave) % (len(idioma)), idioma)
             
    return texto_cifrado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_del_archivo> <clave_de_encriptación>")
        sys.exit(1)
        
    nombre_archivo = sys.argv[1]
    clave = sys.argv[2]
    texto_original = leer_archivo(nombre_archivo)
    
    if texto_original is not None:
        texto_sin_espacios = texto_original.replace(" ", "").replace("\n", "")
        out = descifrado_vigenere(texto_original, clave, spanish_chars)
        print(out)
