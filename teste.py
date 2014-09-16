#! usr/bin/env python
#-*- coding: utf-8 -*-

import Malu
from random import randint

lista = [1, 3, 5, 7, 4, 5, 12, 12, 2, 6, 8, 5, 11, 13, 14, 15, 16, 17, 13 ,11, 10, 15, 21, 23, 25, 27, 30, 34, 32, 31, 35, 36, 41, 42, 44, 41, 46, 47, 48, 49, 55, 52, 53, 54, 57,65, 63, 62, 62, 66, 65, 69, 60]

lista =[20,20,20,20,23,23,23,23,23,24,24,30,30,30,30,30]

lista = []

for i in range(57):
	lista.append(randint(1,40))

lista = ['39', '45', '45', '45', '45', '45', '45', '46', '46', '46', '46', '46', '47', '47', '47', '47', '47', '47', '47', '47', '47', '47', '47', '47', '48', '48', '48', '48', '48', '48', '48', '48', '48', '48', '48', '49', '49', '49', '49', '49', '49', '49', '49', '49', '49', '49', '49', '49', '49', '49', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '51', '51', '51', '51', '51', '51', '51', '51', '51', '51', '52', '52', '52', '52', '52', '53', '53', '53', '53', '53', '54', '55', '55', '57', '58', '58']

for i in range(len(lista)):
	lista[i] = int(lista[i])

r = Malu.Rol(lista)

t = Malu.Dados(r)
print t.Rol.Len
t.Amplitude()
t.NumeroDeClasse()
t.IntervaloDeClasse()
#t.ClassificaDados()
#t.MedidaTendenciaCentral()
#d = t.MedidaTendenciaCentral
d = Malu.Tabela(r, t.Ik, t.K)
'''

d.DadosBruto_Rol()


d.Media()
d.Mediana()
d.Moda()
t.Tabela()
#print t.Rol.Rol
print "\n\nMedia: %5.2f\nMediana: %5.2f" % (d.media, d.mediana)
for i in range(len(d.moda['King'])):
	print "Moda:\n  Convencional: %5.2f\n  King: %5.2f\n  Czuber: %5.2f\n  Pearson: %5.2f" % (d.moda['Convencional'][i], d.moda['King'][i], d.moda['Czuber'][i], d.moda['Pearson'][i])
'''
