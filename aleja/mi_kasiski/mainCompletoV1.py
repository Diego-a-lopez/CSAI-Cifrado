import sys
import os
from math import gcd
from functools import reduce
MAX_KEY_LENGTH_GUESS = 20
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
#alphabet = 'abcdefghijklmnñopqrstuvwxyz'




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
    max_length = 0
    for subcadena in subcadenas:
        es_subcadena = False
        for otra_subcadena in subcadenas:
            if subcadena != otra_subcadena and subcadena in otra_subcadena:
                es_subcadena = True
                break
        if not es_subcadena:
            if (len(subcadena) > max_length):
                max_length = len(subcadena)
            subcadenas_filtradas.append(subcadena)
    return subcadenas_filtradas, max_length


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


def gcd_of_list(numbers):
    if len(numbers) == 0:
        return None  # If the list is empty, return None or handle the case appropriately
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

# FASE 5

def find_caesar_shift(substring, lang):
    max_count = 0
    best_shift = 0
    
    if lang == 'en':
        alphabet_length = 26
        common_letters = 'etaoinshrdlu'
    elif lang == 'fr':
        alphabet_length = 27
        common_letters = 'eariotnsludcmpé'
    elif lang == 'sp':
        alphabet_length = 27
        common_letters = 'eaosrnidltcmupbgé'
    else:
        raise ValueError("Unsupported language. Please choose 'en', 'fr', or 'sp'.")
    
    for shift in range(alphabet_length):
        shifted_text = ''.join(chr((ord(char) - ord('a') - shift) % alphabet_length + ord('a')) for char in substring.lower())
        count = sum(shifted_text.count(letter) for letter in common_letters)
        
        if count > max_count:
            max_count = count
            best_shift = shift
    
    return best_shift

def generate_key(substrings, lang):
    key = ''
    for substring in substrings:
        shift = find_caesar_shift(substring, lang)
        key += chr((26 - shift) % 26 + 97)
    return key
   
# FASE 4

def create_substrings(text, key_length):
    substrings = [''] * key_length
    for i, char in enumerate(text):
        substrings[i % key_length] += char
    return substrings






######## DEL REPO 4

def get_index_c(ciphertext):
	
	N = float(len(ciphertext))
	frequency_sum = 0.0

	# Using Index of Coincidence formula
	for letter in alphabet:
		frequency_sum+= ciphertext.count(letter) * (ciphertext.count(letter)-1)

	# Using Index of Coincidence formula
	ic = frequency_sum/(N*(N-1))
	return ic

# Returns the key length with the highest average Index of Coincidence
def get_key_length(ciphertext):
	ic_table=[]

	# Splits the ciphertext into sequences based on the guessed key length from 0 until the max key length guess (20)
	# Ex. guessing a key length of 2 splits the "12345678" into "1357" and "2468"
	# This procedure of breaking ciphertext into sequences and sorting it by the Index of Coincidence
	# The guessed key length with the highest IC is the most porbable key length
	for guess_len in range(MAX_KEY_LENGTH_GUESS):
		ic_sum=0.0
		avg_ic=0.0
		for i in range(guess_len):
			sequence=""
			# breaks the ciphertext into sequences
			for j in range(0, len(ciphertext[i:]), guess_len):
				sequence += ciphertext[i+j]
			ic_sum+=get_index_c(sequence)
		# obviously don't want to divide by zero
		if not guess_len==0:
			avg_ic=ic_sum/guess_len
		ic_table.append(avg_ic)

	# returns the index of the highest Index of Coincidence (most probable key length)
	best_guess = ic_table.index(sorted(ic_table, reverse = True)[0])
	second_best_guess = ic_table.index(sorted(ic_table, reverse = True)[1])

	# Since this program can sometimes think that a key is literally twice itself, or three times itself, 
	# it's best to return the smaller amount.
	# Ex. the actual key is "dog", but the program thinks the key is "dogdog" or "dogdogdog"
	# (The reason for this error is that the frequency distribution for the key "dog" vs "dogdog" would be nearly identical)
	if best_guess % second_best_guess == 0:
		return second_best_guess
	else:
		return best_guess










###############









if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_del_archivo>")
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    texto_original = leer_archivo(nombre_archivo)
    texto_sin_espacios = texto_original.replace(" ", "").replace("\n", "")

    print("Longitud: "+str(len(texto_sin_espacios)))
    print("TIENE QUE DAR 404")


    # Intento repo 4

    key_length=get_key_length(texto_sin_espacios)
    print("Key length is most likely {}".format(key_length))
    


    
    subcadenas_repetidas = encontrar_subcadenas_repetidas(texto_sin_espacios)
    subcadenas_filtradas, max_length = filtrar_subcadenas(subcadenas_repetidas)

    # ALOMEJOR IMPLEMENTO EL METODO DE SELECCION DE PREFERENCIA PARA MCD
    # Es decir, o que tenia pensado en un principio me lo replantearé



    # Condicion para MCD
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
            
    lang = 'sp'  # or 'fr', or 'sp'
    key = generate_key(substrings, lang)
    print("Posible clave encontrada:", key)
