

# Entradas
english_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
spanish_chars = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
#french_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#print(spanish_chars)
#print(english_chars)
#print(french_chars)

# Prueba clase
txt_a_cifrar = "Hola a todos"
clave = "patata"


# Prueba de un video
#txt_a_cifrar = "criptogramas resueltos"
#clave = "meca"




#### NOTAAA: Offset = Iteracion del bucle de recorrido

# Otener numero de posicion
def charToNumber(letra, idioma):
    # Convertir la letra y la cadena a mayúsculas para hacer la búsqueda insensible a mayúsculas y minúsculas
    letra = letra.upper()
    idioma = idioma.upper()

    
    # Iterar sobre la cadena para buscar la letra
    for numero in range(len(idioma)):
        if idioma[numero] == letra:
            return numero  # Devolver la posición si se encuentra la letra


def numberToChar(numero, idioma):
    return idioma[numero]



# Cifrado Vignere
def cifrado_vigenere(inpuTXT, clave, idioma):
    
    texto_cifrado = "" # Texto de salida
    clave_repetida = "" # Clave que luego se generara a partir de kasiski

    print("Texto a cifrar: "+str(inpuTXT))
    print("Clave: "+str(clave_repetida))
    print("Idioma: "+str(idioma))
    print()


    # Eliminacion de espacios
    inpuTXT = inpuTXT.replace(" ", "")

    # Convertir entradas a mayúsculas
    inpuTXT = inpuTXT.upper()
    clave = clave.upper()
    
    
    for i in range(len(inpuTXT)):
        clave_repetida += clave[i % len(clave)]
    
    
    print("Sin espacios: "+str(inpuTXT))
    print("Clave alargada: "+str(clave_repetida))
    
    
    for i in range(len(inpuTXT)):

        # Obtenemos las posiciones de las letras
        pos_char_texto = charToNumber(inpuTXT[i], idioma)
        pos_char_clave = charToNumber(clave_repetida[i], idioma)
        
        # Cifrado Vigenère ==> Ci= (Mi-Ki) mod N
        texto_cifrado += numberToChar((pos_char_texto + pos_char_clave) % (len(idioma)), idioma)
             
        #print(pos_char_texto)
        #print(pos_char_clave)
        #print(texto_cifrado)
        #print()
        
    
    return texto_cifrado





### Pruebas individuales

# Pruebas charToNumber()

#print(str(charToNumber("A",english_chars, 0))) # 0
#print(str(charToNumber("Ñ",spanish_chars, 0))) # 14
#print()

# Pruebas numberToChar()

#print(str(numberToChar(0, english_chars, 2))) # C
#print(str(numberToChar(14, spanish_chars, 0))) # Ñ

#quit()


######################### EJECUCION

print(len(spanish_chars))

out = cifrado_vigenere(txt_a_cifrar, clave, spanish_chars)
print("Texto cifrado:", out)







