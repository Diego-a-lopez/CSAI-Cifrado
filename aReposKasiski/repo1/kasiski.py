import sys
 


#DESCOMENTAR PARA QUE FUNCIONE INTRODUCIENDO UN TEXTO

#if len(sys.argv) != 2:
#    print("\nUso incorrecto del comando, utilizar la sintaxis:\npython3 kasiski.py cifrado.txt\n")
#    exit()


#file = open(sys.argv[1], 'r')
#text = file.read()

text = 'LFEWCYUGDCUXIGOYYGZHHXICILPSNQVHJMWAIWXCUJEOOAUWTHECWOCYLEKSSUPVGWUXVHHMGPOKLEGOZSGJFAUPVGLHHDSJCWZWZLIXHHHKPZVMHZXHFSNOYYQJXVYRPBIIPXCUUKPOKOVVBAYUPWUWVHWUOXJGLMGPFYYPJGICIIMJIRAWAUPJGHZYZUVMYVJLYRPBHMEMHLHGJBHVYIRHHXZOJYMOSYYXDFHSINQBLVZZVMWJPYYYIDSUXJQBVMZFAIGJBWUTZZHVWJFIYROSKYGJQPHEMSZYVOOSIWXCYNEJQOIXMCGIWYSARMNHVLVVRLFQDGTIXVAHHSLILFSNFLWXVBNOPJGKYTVHHNEXCUORKOSCPGCSUVBCKYFMCJBIOOWCRXVHORMSJNEIUBFSYSWUXVHHOROFVTSYSJBMNHVLVVMVNVJFLWXVBNOPJRLJEOOAUVZDPNIZZWLSXSZIGJBLFVZGAIHZZHMTVHHNENMARMNHVLVVTYCIGCZXIIILPSZBSUQDGTUWVFAYRYCUXICOZZVDHVFENDHNEOOZYWXIYLIGCZMSWFLJEKSSUFNCYVIIHLMEUCUUPVGWUXVHHMGVGJUPJGOOIQCZZVDSWOIYSZBEXSYFSNQVHTPBACPGOVMMISSFETGHTSIOSIWNWYPIZBJUHVDSUXJIUBYZJVORKOYXIKWUWLNRLNBDGAIVMOJIRKOAUXVMBHEKCYWMJBKYPZQOOKVOKIVIOJIRPBHMLJXHMHZDLLIEWSFEQOSUPZQOOKVGLWEOFVWIVMWIRGOLHYIPVFTDQHFEXSIIPGSAUIIXBFMVBHZMIOFUKMSNUPVSUYPHCTYROCKYWZFCCVNOGIRVMHFMIOSUGJBHWIDHLSZDBHAVZQVHWZXVUPVVVLEYSJIRAWAUVGOZJEOOAUWZGPGTJFAUROSXOINSOUKVBWIVYSUNVJMXOIICZYHJFLHTMSCCIISLFINHYYRDAPYROCFGIECYUIGDYIGZGVXMBSZNMQCMUZJFLWMZBKIPVTBHGDCUBIKOACGVTHPSMSJYIGQYYGDAPYROCVMIJMTCRZFHFMUOJCSIRLFSNVBYWJGZCIIRVGYTWTJSMHHHXZSUFEZRHXMITHHXDZFYRGOZJIMGVHENAHSSMSZR'

pentahashmap = {}
cuatrihashmap = {}    
trihashmap = {}

# Vamos a utilizar pentagramas, cuatrigramas y trigramas en esta implementación.


# Cálculo apariciones de pentagramas

for index in range(len(text)-4):
    
    count = 0
    pentagram = text[index]+text[index+1]+text[index+2]+text[index+3]+text[index+4]
    for auxindex in range(len(text)-4):
        if auxindex != 0:
            auxpentagram = text[auxindex]+text[auxindex+1]+text[auxindex+2]+text[auxindex+3]+text[auxindex+4]
            if pentagram == auxpentagram:
                count+=1
                pentahashmap [pentagram] = count

for i in pentahashmap.copy():
        if pentahashmap[i] == 1 or pentahashmap[i] == 2:  # Eliminamos los cuatrigramas que menos se repiten, esto se puede cambiar para tener distintas precisiones
            pentahashmap.pop(i)   


# En esta parte, result será un string que en cada salto de línea presentaremos el índice de todas las ocurrencias de los cuatrigramas.

result = ''   
for i in pentahashmap:
    for j in range(pentahashmap[i]):
        offset = -1
        while True:
            try:
                offset = text.index(i, offset+1)
            except ValueError: # No hay más ocurrencias, por lo que metemos un salto de línea y avanzamos al siguiente cuatrigrama
                result += '\n'
                break
            result += str(offset) + ' '

result2 = result.split('\n')
mcdNumbers = []
for i in range(len(result2)-1):
    if(i%8 == 0): # Si eliminamos hasta los pentagramas con 2 repeticiones, es i%3, si NO los eliminamos, es i%2
        n1 = int(result2[i].split(' ')[0])
        n2 = int(result2[i].split(' ')[1])
        n3 = int(result2[i].split(' ')[2])

        try:  # En este try se decide que no vamos a guardar mas de 4 indices del mismo pentagramas
            n4 = int(result2[i].split(' ')[3])
        except ValueError or IndexError:
            d1 = n3-n2
            d2 = n2-n1
            mcdNumbers.append(d1)
            mcdNumbers.append(d2)

# Cálculo de MCD para saber la longitud de la clave

mcd5Flag = False
if len(mcdNumbers) > 1:
    mcd5Flag = True 


def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

gc3=0

for i in range(round(len(mcdNumbers))):
    gc3=find_gcd(gc3, mcdNumbers[i])
    
mcd5 = gc3

# Cálculo apariciones de cuatrigramas

for index in range(len(text)-3):
    
    count = 0
    cuatrigram = text[index]+text[index+1]+text[index+2]+text[index+3]
    for auxindex in range(len(text)-3):
        if auxindex != 0:
            auxcuatrigram = text[auxindex]+text[auxindex+1]+text[auxindex+2]+text[auxindex+3]
            if cuatrigram == auxcuatrigram:
                count+=1
                cuatrihashmap [cuatrigram] = count

for i in cuatrihashmap.copy():
        if cuatrihashmap[i] == 1 or cuatrihashmap[i] == 2:  # Eliminamos los cuatrigramas que menos se repiten, esto se puede cambiar para tener distintas precisiones
            cuatrihashmap.pop(i)   


# En esta parte, result será un string que en cada salto de línea presentaremos el índice de todas las ocurrencias de los cuatrigramas.

result = ''   
for i in cuatrihashmap:
    for j in range(cuatrihashmap[i]):
        offset = -1
        while True:
            try:
                offset = text.index(i, offset+1)
            except ValueError: # No hay más ocurrencias, por lo que metemos un salto de línea y avanzamos al siguiente cuatrigrama
                result += '\n'
                break
            result += str(offset) + ' '

result2 = result.split('\n')
mcdNumbers = []
for i in range(len(result2)-1):
    if(i%3 == 0): # Si eliminamos hasta los cuatrigramas con 2 repeticiones, es i%3, si NO los eliminamos, es i%2
        n1 = int(result2[i].split(' ')[0])
        n2 = int(result2[i].split(' ')[1])
        n3 = int(result2[i].split(' ')[2])

        try:  # En este try se decide que no vamos a guardar mas de 4 indices del mismo cuatrigrama
            n4 = int(result2[i].split(' ')[3])
        except ValueError or IndexError:
            d1 = n3-n2
            d2 = n2-n1
            mcdNumbers.append(d1)
            mcdNumbers.append(d2)

        
# Cálculo de MCD para saber la longitud de la clave


gc1=0

mcd4Flag = False
if len(mcdNumbers) > 1:
    mcd4Flag = True 

for i in range((len(mcdNumbers))): 
    gc1=find_gcd(gc1, mcdNumbers[i])

mcd4 = gc1

# Cálculo apariciones de trigramas, mismo planteamiento

for index in range(len(text)-2):
    
    count = 0
    cuatrigram = text[index]+text[index+1]+text[index+2]
    for auxindex in range(len(text)-2):
        if auxindex != 0:
            auxcuatrigram = text[auxindex]+text[auxindex+1]+text[auxindex+2]
            if cuatrigram == auxcuatrigram:
                count+=1
                trihashmap [cuatrigram] = count


for i in trihashmap.copy():
        if trihashmap[i] == 1 or trihashmap[i] == 2 or trihashmap[i] == 3 or trihashmap[i] == 4: # Eliminamos los trigramas que menos se repiten, esto se puede cambiar para tener distintas precisiones
            trihashmap.pop(i)


result = ''   
for i in trihashmap:
    for j in range(trihashmap[i]):
        offset = -1
        while True:
            try:
                offset = text.index(i, offset+1)
            except ValueError: # No hay más ocurrencias, por lo que metemos un salto de línea y avanzamos al siguiente cuatrigrama
                result += '\n'
                break
            result += str(offset) + ' '

result2 = result.split('\n')
mcdNumbers = []
for i in range(len(result2)-1):
    if(i%3 == 0): # Si eliminamos hasta los cuatrigramas con 2 repeticiones, es i%3, si NO los eliminamos, es i%2
        n1 = int(result2[i].split(' ')[0])
        n2 = int(result2[i].split(' ')[1])
        n3 = int(result2[i].split(' ')[2])

        try:  # En este try se decide que no vamos a guardar mas de 4 indices del mismo cuatrigrama
            n4 = int(result2[i].split(' ')[3])
        except ValueError or IndexError:
            d1 = n3-n2
            d2 = n2-n1
            mcdNumbers.append(d1)
            mcdNumbers.append(d2)
       
        
# Cálculo de MCD para saber la longitud de la clave
gc1=0
gc2=0
gc3=0
#Vamos a hacer grupos de longitudes para intentar evitar distancias falsas
for i in range((len(mcdNumbers)-round((len(mcdNumbers)/2)))): # principio a mitad
    gc1=find_gcd(gc1, mcdNumbers[i])
for i in range(round(len(mcdNumbers)/2), len(mcdNumbers)): # mitad a final
    gc2=find_gcd(gc2, mcdNumbers[i])
for i in range(len(mcdNumbers)): # todo
    gc3=find_gcd(gc3, mcdNumbers[i])
# Cogemos el mayor mcd de los tres
mcd3 = max(gc1,gc2,gc3)




            ########################## Operación comun #################################


mcdlist = [mcd3, mcd4, mcd5]


for i in range(len(mcdlist)-1):
    if mcdlist[i] == 0 or mcdlist[i] == 1:
        mcdlist.pop(i)


if(mcd5Flag):
    mcd = mcd5    
elif(mcd4Flag):
    mcd = mcd4   
else:
    mcd = mcd3


if(mcd == 0):
    exit('No es posible encontrar la longitud de la clave, cerrando programa...')

# División en subcriptogramas

subcrypt = []
for i in range(mcd):
    subcrypt.append([]) 

size = 0
while(size != len(text)+mcd):
    try:
        for i in range(mcd):
            subcrypt[i].append(text[size])
            size+=1
    except IndexError:
        break

size = len(text)-(mcd-1) # Últimas letras del texto
try:
    for i in range(mcd):
        subcrypt[i].append(text[size])
        size+=1
except IndexError:
    pass        


##### ANÁLISIS DE FRECUENCIAS #####

frecuencias = []
for i in range(mcd):
    frecuencias.append({'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 
        'E': 0.0, 'F': 0.0, 'G': 0.0, 'H': 0.0, 'I': 0.0, 'J': 0.0, 
        'K': 0.0, 'L': 0.0, 'M': 0.0, 'N': 0.0, 'O': 0.0, 'P': 0.0, 
        'Q': 0.0, 'R': 0.0, 'S': 0.0, 'T': 0.0, 'U': 0.0, 'V': 0.0, 
        'W': 0.0, 'X': 0.0, 'Y': 0.0, 'Z': 0.0}) 


for i in range(mcd):
    for key in frecuencias[i].keys(): # Coge de la A-Z
        for letter in subcrypt[i]: # Coge las letras del subcriptograma
            if letter == key: # Si coinciden se suma 1
                frecuencias[i][key] += 1

for i in range(mcd):
    for j in frecuencias[i].keys():
        frecuencias[i][j] = (frecuencias[i][j] / 26)


maximoSubcriptograma = [] # Lista con los máximos
for i in range(mcd):
    maximoSubcriptograma.append('')


# Momento de tirarse un triple dando por hecho que la frecuencia más alta será, por estadística la 'E'. Sólo textos en Español !!!!
for index in range(mcd):
    max = 0
    for i in frecuencias[index].keys():
        if frecuencias[index][i] > max:
            maximoSubcriptograma[index] = str(i)
            max = frecuencias[index][i]

# Si el caracter del subcriptograma en frecuencia tiene a 4 posiciones a su derecha a otra letra la cual
# tiene un valor de al menos un 75% del máximo, suponemos que la relación es A->E. Dado que la clave del cifrado desplaza N posiciones,
# la letra de la clave va a ser la 'A' en cada subcriptograma
for i in range(mcd):
    if frecuencias[i][chr((((ord(maximoSubcriptograma[i]) - 65) - 4) % 26) + 65)] > 0.75 * frecuencias[i][maximoSubcriptograma[i]]: # Si es verdad, A->E
        maximoSubcriptograma[i] = chr((((ord(maximoSubcriptograma[i]) - 65 - 4) % 26) + 65))

posibleClave = ''
for i in range(mcd):
    posibleClave += maximoSubcriptograma[i]

print('\n'+'La clave puede ser: ' + posibleClave+'\n')
