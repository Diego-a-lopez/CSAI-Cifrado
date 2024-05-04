#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
import math
import random
import archivo

### Metodos para cifrar

def imprimir(matriz,n):
	i=0
	j=0
	while(i<n):
		ma=""
		while(j<n):
			ma=ma+matriz[i][j]
			j=j+1
		print (ma)
		j=0
		i=i+1

def verificarMascara(m,m2,m3,m4):
	i=0
	numX=0
	while(i<len(m)):
		j=0
		while(j<len(m)):
			rep=0
			if(m[i][j].upper()=="X"):
				rep=rep+1
			if(m2[i][j].upper()=="X"):
				rep=rep+1
			if(m3[i][j].upper()=="X"):
				rep=rep+1
			if(m4[i][j].upper()=="X"):
				rep=rep+1
			if(rep>1):
				print ("Hay coincidencia en la perforacion",i,",",j," al rotarla")
				sys.exit()
			j=j+1
		i=i+1
			

def rotar(matriz,n):
	nueva=[]
	for i in range(n):
		nueva.append(["-"]*n)
	i=0
	j=n-1
	while(i<n and j>=0):
		k=0
		while(k<n):
			nueva[k][j]=matriz[i][k]
			k=k+1
		i=i+1
		j=j-1
	return nueva

def hubicarLetras(matriz,mascara,mensaje,l):
	i=0
	j=0
	letra=l
	while(i<len(mascara)):
		j=0
		while(j<len(mascara)):
			if(mascara[i][j].upper()=="X"):
				if(letra<len(mensaje)):
					matriz[i][j]=mensaje[letra]
				else:
					matriz[i][j]="$"
				letra=letra+1
			j=j+1
		i=i+1

def completrar(matriz,mensaje,tam):
	i=0
	j=0
	while(i<len(matriz)):
		j=0
		while(j<len(matriz)):
			if(matriz[i][j]=="null"):
				matriz[i][j]=mensaje[random.randint(0,tam-1)]
			j=j+1
		i=i+1	

def generarCif(matriz,cod):
	i=0
	j=0
	cif=""
	while(i<len(matriz)):
		j=0
		while(j<len(matriz)):
			if(cod=="" or matriz[i][j]=="$"):
				cif=cif+matriz[i][j]
			else:		
				#print (matriz[i][j])	
				cif=cif+chr(matriz[i][j])
			j=j+1
		i=i+1
	return cif

def llenarMacara(mascara,perf):
	i=1
	while(i<len(perf)):
		aux=perf[i].split(",")
		mascara[int(aux[0])][int(aux[1])]="X"
		i=i+1

def cifradoMR(arch,masc,cod):
	mensaje=""
	perforaciones=[]
	if(cod==""):
		f = archivo.abrirArchivo(arch)
	else:
		f = archivo.abrirArchivo64(arch)
	p = archivo.abrirArchivo(masc)
	if f=='' or p=='':
		if f=='':
			print ('No se encontro el archivo ',arch)
		if p=='':
			print ('No se encontro el archivo ',masc)
		sys.exit()
	if(cod==""):	
		for pal in f.readlines():
			mensaje=mensaje+pal
		f.close()
	else: mensaje=f
	numC=len(mensaje)
	n=int(math.ceil(math.sqrt(numC)))
	for per in p.readlines():
		perforaciones.append(per)
	p.close()
	if(int(perforaciones[0])<n):
		print ("El tamaño de la matriz es muy pequeño, debe tener un tamaño minimo de ",n)
		sys.exit()
	x=int(numC/4)
	if(x<(numC/4.0)):
		x=x+1
	if((len(perforaciones)-1)!=x):
		print ("El numero de perforaciones 'X' no es el correcto")
		print ("La mascara debe tener ",x," perforaciones"," y tiene :",(len(perforaciones)-1))
		sys.exit()	
	matriz=[]
	mascara=[]
	n=int(perforaciones[0])
	for i in range(n):
		matriz.append(["null"]*n)
		mascara.append(["-"]*n)
	llenarMacara(mascara,perforaciones)
	if(len(mascara)==n and len(mascara[i])==n):
		mascara2=rotar(mascara,n)
		mascara3=rotar(mascara2,n)
		mascara4=rotar(mascara3,n)
	else:
		print ("La mascara debe tener tamaño ",n,"x",n)
		sys.exit()
	verificarMascara(mascara,mascara2,mascara3,mascara4)
	numP=len(perforaciones)-1
	l=0
	hubicarLetras(matriz,mascara,mensaje,l)
	l=l+numP
	hubicarLetras(matriz,mascara2,mensaje,l)
	l=l+numP
	hubicarLetras(matriz,mascara3,mensaje,l)
	l=l+numP
	hubicarLetras(matriz,mascara4,mensaje,l)
	l=l+numP
	completrar(matriz,mensaje,numC)
	cif=generarCif(matriz,cod)
	sal = arch+".cif"
	print (sal)
	fichero = archivo.escribirArchivo(sal, cif)
	if fichero=='':
		print ('Ocurrio un error al intentar escribir en ', n)
	else:
		fichero.close()
		print ("\n*********************************************************************")
		print ("  SE GENERO EL ARCHIVO ", sal," CON EL MENSAJE CIFRADO")
		print ("*********************************************************************\n\n")


### Metodos para descifrar

def llenarMatriz(matriz,mensaje,n):
	i=0
	j=0
	cont=0
	while(i<n):
		while(j<n):
			matriz[i][j]=mensaje[cont]
			j=j+1
			cont=cont+1
		j=0
		i=i+1

def consMensaje(matriz,mascara):
	i=0
	j=0
	men=""
	while(i<len(mascara)):
		while(j<len(mascara)):
			if(mascara[i][j].upper()=="X"):
				if(matriz[i][j]!="$"):
					men=men+matriz[i][j]
				else:
					return men
			j=j+1
		j=0
		i=i+1
	return men

def descifradoMR(arch,masc,cod):
	mensaje=""
	perforaciones=[]
	f = archivo.abrirArchivo(arch)
	p = archivo.abrirArchivo(masc)
	if f=='' or p=='':
		print ('No se encontro el archivo ',arch)
		sys.exit()
	for pal in f.readlines():
		mensaje=mensaje+pal
	f.close()
	numC=len(mensaje)
	n=int(math.ceil(math.sqrt(numC)))
	for per in p.readlines():
		perforaciones.append(per)
	p.close()
	if(int(perforaciones[0])<n):
		print ("El tamaño de la matriz es muy pequeño, debe tener un tamaño minimo de ",n)
		sys.exit()
	matriz=[]
	mascara=[]
	n=int(perforaciones[0])
	for i in range(n):
		matriz.append(["null"]*n)
		mascara.append(["-"]*n)
	llenarMatriz(matriz,mensaje,n)
	llenarMacara(mascara,perforaciones)
	mascara2=rotar(mascara,n)
	mascara3=rotar(mascara2,n)
	mascara4=rotar(mascara3,n)
	verificarMascara(mascara,mascara2,mascara3,mascara4)
	men=""
	men=men+consMensaje(matriz,mascara)
	men=men+consMensaje(matriz,mascara2)
	men=men+consMensaje(matriz,mascara3)
	men=men+consMensaje(matriz,mascara4)
	sal = arch.replace("cif","dec")
	if(cod==""):
		fichero = archivo.escribirArchivo(sal,men)
	else:
		fichero = archivo.escribirArchivo64(sal,men)		
	if fichero=='':
		print ('Ocurrio un error al intentar escribir en ', sal)
	else:
		fichero.close()
		print ("\n*********************************************************************")
		print ("SE GENERO EL ARCHIVO ",sal," CON EL MENSAJE EN CLARO")
		print ("*********************************************************************\n\n\n")
