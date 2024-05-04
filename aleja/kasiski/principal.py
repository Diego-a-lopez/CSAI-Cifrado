#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys 

import ayuda
import validaciones

from kasiski import metodo_kasiski

numArg=len(sys.argv)
arg=sys.argv

if(numArg==1):
	ayuda.ayudaPrincipal()

elif numArg== 3:
	if arg[1] == "-k":
		metodo_kasiski(arg[2])

elif(numArg==2):
	if (arg[1] == "-k"):
		ayuda.ayudaKasiski()
		print("")
	
else:
	if(arg[1]=="-k"):
		validaciones.validacionKasiski(arg)
	else:
		print ("EL COMANDO QUE DIGITÓ NO ES UNA OPCION VÁLIDA")
