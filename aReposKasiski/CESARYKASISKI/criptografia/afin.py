# -*- coding: utf8 -*-
import os, sys
import archivo
import alfabeto

TAM_ALFABETO = alfabeto.tamAlfabeto()
abc = alfabeto.getAlfabeto()

def cifrarAfin(texto, a, b, nombreArchivoSalida, cod):
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
			modulo = (a*mi+b)%TAM_ALFABETO
			mensajeCifrado = mensajeCifrado + abc[modulo]
			i+=1
	if(flag==-1):
		print("La ejecución se detuvo") 
	else:
		f = archivo.escribirArchivo(nombreArchivoSalida, mensajeCifrado)
		if f=='':
			print ('Ocurrio un error al intentar escribir en', nombreArchivoSalida)
		else:
			print ('Se guardo correctamente el mensaje cifrado en', nombreArchivoSalida)
			f.close()
	sys.stdin.flush()
	
def descifrarAfin(texto, a, b, nombreArchivoSalida, cod):
	x = modinv(a,TAM_ALFABETO)
	mensajeClaro = ""
	i = 0
	while (i < len(texto)):
		ci = alfabeto.getPosicion(texto[i])
		modulo = (x*(ci-b))%TAM_ALFABETO
		mensajeClaro = mensajeClaro + abc[modulo]
		i+=1
	if(cod==""):
		f = archivo.escribirArchivo(nombreArchivoSalida,mensajeClaro)
		f.close()
	else:
		f = archivo.escribirArchivo64(nombreArchivoSalida,mensajeClaro)
	if f=='':
		print ('Ocurrio un error al intentar escribir en', nombreArchivoSalida)
	else:
		print ('Se guardo correctamente el mensaje descifrado en',nombreArchivoSalida)
	sys.stdin.flush()
	

def verificarCoprimo(a):
	d,x,y = mcd(a,TAM_ALFABETO)
	if d == 1:
		return True
	else:
		return False


"""--- Código tomado de https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49 ---"""
"""  ------------------------      Realizado por Olivier FAURAX     ------------------------"""
def mcd(a, b):
	if a == 0:
		return (b, 0, 1)
	g, y, x = mcd(b%a,a)
	return (g, x - (b//a) * y, y)

def modinv(a, m):
	g, x, y = mcd(a, m)
	if g != 1:
		raise Exception('No modular inverse')
	return x%m
"""  ------------------------          ------------------------"""

def obtenerA(valor):
	a = 0
	try:
		a = int(valor)
	except ValueError:
		print ("Ingresa un número entre 1 y ",TAM_ALFABETO-1," para 'a'")
		return -1
	else:
		if (a >= 0 and a < TAM_ALFABETO):
			return a
		else:
			print ('Ingresa un número entre 1 y ',TAM_ALFABETO-1," para 'a'")
			return -1

def obtenerB(valor):
	a = 0
	try:
		a = int(valor)
	except ValueError:
		print ("Ingresa un número entre 1 y ",TAM_ALFABETO-1," para 'b'")
		return -1
	else:
		if (a >= 0 and a < TAM_ALFABETO):
			return a
		else:
			print ('Ingresa un número entre 1 y ', TAM_ALFABETO-1," para 'b'")
			return -1
