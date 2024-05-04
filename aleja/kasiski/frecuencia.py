#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
import archivo
import alfabeto
import operator

TAM_ALFABETO = alfabeto.tamAlfabeto()
abc = alfabeto.getAlfabeto()
frecuAlta = ['E','A','S','O', 'I', 'N', 'R', 'D', 'T']

	
def analisisFrecuencia(criptograma, nomArchivoSalida):
	listaFrecu = frecuencias(criptograma)
	k = verificarHipostesis(listaFrecu)
	print ('La clave con la que se cifró es: ',k)
	mensajeClaro = ""
	i=0
	while (i < len(criptograma)):
		ci = alfabeto.getPosicion(criptograma[i])
		modulo = (ci-k)%TAM_ALFABETO
		mensajeClaro = mensajeClaro + abc[modulo]
		i+=1
	f = archivo.escribirArchivo(nomArchivoSalida,mensajeClaro)
	if f=='':
		print ('Ocurrio un error al intentar escribir en', nomArchivoSalida)
	else:
		print ('El mensaje descifrado se guardo correctamente en',nomArchivoSalida)
	#print mensajeClaro
		
		
def verificarHipostesis(listaFrecu):
	K = 0
	k1 = 0
	k2 = 0
	for i in frecuAlta:
		for j in frecuAlta:
			if (i!=j):
				k1 = encontrarK(i, listaFrecu[0][0])
				k2 = encontrarK(j, listaFrecu[1][0])
				if(k1==k2):
					return k1
					break
				else:
					k1 = encontrarK(j, listaFrecu[0][0])
					k2 = encontrarK(i, listaFrecu[1][0])
					if(k1==k2):
						return k1
						break


def encontrarK(letraMi, letraCi):
	mi = alfabeto.getPosicion(letraMi)
	ci = alfabeto.getPosicion(letraCi)
	return (ci-mi)%TAM_ALFABETO

def contar(letra, texto):
	contador = 0
	i = 0
	while (i < len(texto)):
		if texto[i] == '\xc3' or texto[i] == '\xc2':
			caracter = texto[i] + texto[i + 1]
			i+=1
		else:
			caracter = texto[i]
		if caracter == letra:
				contador = contador + 1
		i+=1
	return contador

def frecuencias(texto):
	listaFrecuencias = {}
	i = 0
	while (i < len(abc)):
		n = contar(abc[i],texto)
		if (n != 0):
			listaFrecuencias[abc[i]] = n
		i+=1
	resultado =  sorted(listaFrecuencias, key=listaFrecuencias.get, reverse=True)
	return resultado	

