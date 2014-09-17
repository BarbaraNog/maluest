#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
import Malu

limpar = "clear"

def CreateRol():
	global Rol
	Cabecalho()
	lenRol = int(raw_input(' Tamanho da coleção: > '))
	if lenRol == 0:
		lenRol = 1000
	print " .Leitura dos dados:"
	for i in range(lenRol):
		try:
			Rol.append(int(raw_input('%4d > ' %(i+1))))
		except:
			break

def ReadRol():
	print rol

def UpdateRol():
	print rol

def DeleteRol():
	rol = []

def Tabela(self):
	intervalo = self.rol[0]
	F = 0
	_F = 0.0
	print '  Cls  |  Int. Classes  |   fi   |   fr %   |   F   |    F %'
	print '-------+----------------+--------+----------+-------+-----------'
	for i in range(self.K):
		F += len(self.listaDeIntervalo[i])
		_F += float(len(self.listaDeIntervalo[i]))/float(self.lenColecao)
		print ('  %3d  |  %4d |- %4d  |  %4d  |  %6.3f  |  %3d  |  %7.3f') % (i+1, intervalo + (self.Ik *i), intervalo + (self.Ik * (i +1)),len(self.listaDeIntervalo[i]), float(len(self.listaDeIntervalo[i]))/float(self.lenColecao)*100, F, _F*100) 

def TabelaVQD(self):
	aux = []
	for i in self.rol:
		if i not in aux:
			aux.append(i)
	F = 0
	_F = 0.0
	print '  x(i)  |   fi   |   fr %   |   F   |    F %'
	print '--------+--------+----------+-------+-----------'
	for i in aux: 
		F += self.rol.count(i)
		_F += float(self.rol.count(i))/float(self.lenColecao) * 100
		print ('  %4d  |  %4d  |  %6.3f  |  %3d  |  %7.3f') % (i, self.rol.count(i),  float(self.rol.count(i))/float(self.lenColecao) * 100, F, _F)

def Cabecalho():
	system("clear")
	print "\n  MaluEst =)                         Desenvolvido por: Pedro Ramon"
	print "--------------------------------------------------------------------\n\n"

Rol = []
while (True):
	system(limpar)
	print "===================================================================="
	print ""
	print "                         Sistema da Malu =)                         "
	print ""
	print "====================================================================\n"
	print " | Menu:"
	print ' +--------------------------------------------------------->\n'
	print " [D/d] Variável Quantitativa Dicreta (Muita Repetição)"
	print " [C/c] Variável Quantitativa Continua (Pouca Repetição)"
	print " [A/a] Detectar no leitura do Rol"
	print " [L/l] Ler uma tabela"
	print " [S/s] Sair"

	opc = raw_input("\n >")

	system(limpar)

	if opc.upper() == 'D':
		


		CreateRol()
		print 'Os dados ordenados ficaram assim:\n'
		print d.rol.Imprimir()
		print '\n' * 2
	
		print 'A apartir disso chegamos aos seguintes valores:\n'
		print '  | Amplitude:       %4d' % d.At
		print '  | N. de Classes:   %4d' % d.K
		print '  | Int. de Classes: %4d' % d.Ik 
		print '\n' * 2
		
		print 'E tambem montamos essa tabela para voce:\n'
		d.Tabela()
		
		print '\n' * 5
		input('Digite "Enter" para sair...')
	elif opc.upper() == 'C':
		print 'Os dados ordenados ficaram assim:\n'
		print d.rol
		print '\n' * 2
		
		print 'E tambem montamos essa tabela para voce:\n'
		d.TabelaVQD()
		
		print '\n' * 5
	elif opc.upper() == 'S':
		system(limpar)
		break
