#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
import archivo
import alfabeto
import base64
from archivo import escribirArchivo

alfabeto = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16,
    'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
}


# alfabeto = {
#     'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
#     'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
#     'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
#     'Y': 24, 'Z': 25
# }

def descifrar_letra(letra, clave):
    valor_descifrado = (alfabeto.get(letra) + alfabeto.get(clave)) % len(alfabeto)
    for letra_alfabeto, valor_alfabeto in alfabeto.items():
        if valor_alfabeto == valor_descifrado:
            return letra_alfabeto


def metodo_vigenere():
    texto = "CGOEDANGTPBZAESZSMCGSHWVNGBCINGGSAPJEWOKEWKRVTGXEYFMEESLIFJCANOYIEIGRTOKVTKZDMHMNMARGYWWIÑOCAXWEADSHRPHVNFOSAGBRSPGHIPBLENDRQGSKEFGRGMPRAGBRFTSJAPBVLWWSRAHVAQWJMMPRLMHVRBWVNFSSOMHVTDOXAEJHRPHREYIVRMHZNXOKTTQRRWOCUPU"
    clave = "AMOR"
    texto_clave = clave * len(texto)
    texto_clave = texto_clave[:len(texto)]

    mensaje_encriptado = ''
    for posicion in range(len(texto)):
        mensaje_encriptado += descifrar_letra(texto[posicion], texto_clave[posicion])
    escribirArchivo('textos_prueba/texto_cifrado.txt', mensaje_encriptado)


def cifraVigenere(archEnt, clave, archSal, cod):
    doc = archEnt
    palabra = ""
    k = ""
    if (cod == ""):
        f = archivo.abrirArchivo(doc)
    else:
        f = archivo.abrirArchivo64(doc)
    h = archivo.abrirArchivo(clave)
    if f == '' or h == '':
        if (f == ''):
            print('No se encontro el archivo ' + doc)
        else:
            print('No se encontro el archivo ' + clave)
    else:
        if (cod == ""):
            for pal in f.readlines():
                palabra = palabra + pal
            f.close()
        else:
            palabra = f
        for cla in h.readlines():
            k = k + cla
        h.close()
        lk = len(k)
        i = 0
        j = 0
        c = ""
        lg = len(palabra)
        alf = alfabeto.getAlfabeto()
        la = alfabeto.tamAlfabeto()
        flag = 1
        # imprimirTexto(palabra)
        # try:
        while (i < lg):
            if (j < lk):
                if (cod == ""):
                    dato = alf[((alf.index(palabra[i]) + alf.index(k[j])) % la)]
                else:
                    p1 = chr(palabra[i])
                    dato = alf[((alf.index(p1) + alf.index(k[j])) % la)]
                c = c + dato
            else:
                if (cod == ""):
                    dato = alf[((alf.index(palabra[i]) + alf.index(palabra[j - lk])) % la)]
                else:
                    p1 = chr(palabra[i])
                    p2 = chr(palabra[j - lk])
                    dato = alf[((alf.index(p1) + alf.index(p2)) % la)]
                c = c + dato
            i = i + 1
            j = j + 1
        if (flag != -1):
            n = archSal
            fichero = archivo.escribirArchivo(n, c)
            if fichero == '':
                print('Ocurrio un error al intentar escribir en ', n)
            else:
                fichero.close()
                print("\n*********************************************************************")
                print("  SE GENERO EL ARCHIVO ", n, " CON EL MENSAJE CIFRADO")
                print("*********************************************************************\n\n")
        else:
            print("La ejecución se detuvo")


# -------------------------------------------------
def descVigenere(archEnt, clave, archSal, cod):
    doc = archEnt
    palabra = ""
    k = ""
    f = archivo.abrirArchivo(doc)
    h = archivo.abrirArchivo(clave)
    if f == '' or h == '':
        if (f == ''):
            print('No se encontro el archivo ' + doc)
        else:
            print('No se encontro el archivo ' + clave)
    else:
        for pal in f.readlines():
            palabra = palabra + pal
        f.close()
        lg = len(palabra)
        for cla in h.readlines():
            k = k + cla
        h.close()
        lk = len(k)
        i = 0
        j = 0
        m = ""
        alf = alfabeto.getAlfabeto()
        la = alfabeto.tamAlfabeto()
        while (i < lg):
            if (j < lk):
                dato = alf[((alf.index(palabra[i]) - alf.index(k[j])) % la)]
                m = m + dato
            else:
                dato = alf[((alf.index(palabra[i]) - alf.index(m[j - lk])) % la)]
                m = m + dato
            i = i + 1
            j = j + 1
        n = archSal
        if (cod == ""):
            fichero = archivo.escribirArchivo(n, m)
        else:
            fichero = archivo.escribirArchivo64(n, m)
        if fichero == '':
            print('Ocurrio un error al intentar escribir en ', n)
        else:
            fichero.close()
            print("\n*********************************************************************")
            print("SE GENERO EL ARCHIVO ", n, " CON EL MENSAJE EN CLARO")
            print("*********************************************************************\n\n\n")


def imprimirTexto(texto):
    i = 0
    print("-------------------------------------------")
    while (i < 200):
        print(texto[i])
        i = i + 1


# cifraVigenere("textos_prueba/quijote.txt","textos_prueba/clave.txt","textos_prueba/quijote.txt.cif","-c64")

if __name__ == '__main__':
    texto = ""
    clave = ""
    texto_clave = clave * len(texto)
    texto_clave = texto_clave[:len(texto)]

    mensaje_encriptado = ''
    for posicion in range(len(texto)):
        mensaje_encriptado += descifrar_letra(texto[posicion], texto_clave[posicion])
    escribirArchivo('textos_prueba/texto_cifrado.txt', mensaje_encriptado)
