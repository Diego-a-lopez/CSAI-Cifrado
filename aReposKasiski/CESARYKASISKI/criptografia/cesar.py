#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
import archivo
import alfabeto

TAM_ALFABETO = alfabeto.tamAlfabeto()
abc = alfabeto.getAlfabeto()
	
def cifrarCesar(texto, clave, nombreArchivoSalida, cod):
	mensajeCifrado = ""
	flag = 1
	i = 0
	while (i < len(texto)):
		if(cod=="-c64"):
			mi = alfabeto.getPosicion(chr(texto[i]))
		else:
			mi = alfabeto.getPosicion(texto[i])
		if(mi==-1):
			if(cod=="-c64"):
				print("El caracter ",chr(texto[i])," no se encuentra en el alfabeto, revise la ayuda en el menú principal para añadirlo") 
			else:
				print("El caracter ",texto[i]," no se encuentra en el alfabeto, revise la ayuda en el menú principal para añadirlo") 
			flag = -1
			break
		else:
			modulo = (mi+clave)%TAM_ALFABETO
			mensajeCifrado = mensajeCifrado + abc[modulo]
			i+=1
	if(flag==-1):
		print("La ejecución se detuvo") 
	else:
		f = archivo.escribirArchivo(nombreArchivoSalida, mensajeCifrado)
		if f =='':
			print ('Ocurrio un error al intentar escribir en', nombreArchivoSalida)
		else:
			print ('El mensaje cifrado se guardo correctamente en',nombreArchivoSalida)
			f.close()
	sys.stdin.flush()

def descifrarCesar(criptograma, clave, nombreArchivoSalida, cod):
	mensajeClaro = ""
	i = 0
	while (i < len(criptograma)):
		ci = alfabeto.getPosicion(criptograma[i])
		modulo = (ci-clave)%TAM_ALFABETO
		mensajeClaro = mensajeClaro + abc[modulo]
		i+=1
	if(cod==""):
		f = archivo.escribirArchivo(nombreArchivoSalida,mensajeClaro)
	else:
		f = archivo.escribirArchivo64(nombreArchivoSalida,mensajeClaro)
	if(f==-1):
		print ('El mensaje no fue codificado antes de cifrar\nLa ejecución se detuvo')
	elif f=='':
		print ('Ocurrio un error al intentar escribir en', nombreArchivoSalida)
	else:
		print ('El mensaje descifrado se guardo correctamente en',nombreArchivoSalida)
		f.close()	
	sys.stdin.flush()
	
def obtenerEntero(cla):
	clave = 0
	try:
		clave = int(cla)
	except ValueError:
		print ("Ingresa un numero entre 1 y \n",TAM_ALFABETO-1)
		return -1
	else:
		if (clave >= 0 and clave < TAM_ALFABETO):
			return clave
		else:
			print ('Ingresa un numero entre 1 y \n', TAM_ALFABETO-1)
			return -1
