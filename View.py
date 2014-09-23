#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
from Malu import *

limpar = "clear"
erro = ""

def CreateRol():
    Rol = []
    CabecalhoMini()
    lenRol = int(raw_input(' Tamanho da coleção: > '))
    if lenRol == 0:
        lenRol = 1000
    print " .Leitura dos dados:"
    for i in range(lenRol):
        try:
            Rol.append(int(raw_input('%4d > ' %(i+1))))
        except:
            break
    return Rol

def TabelaDiscreta():
    erro = "Não Implementado"
    pass

def TabelaContinua():
    erro = "Não Implementado"

def CabecalhoMini():
    global erro
    system(limpar)
    print "\n  MaluEst =)               Estatística Aplicada | FATEC-Franca"
    print "--------------------------------------------------------------------\n\n"
    if erro != "":
        print erro
        erro = ""

def Cabecalho():
    global erro
    system(limpar)
    print "===================================================================="
    print ""
    print "                         Sistema da Malu =)                         "
    print ""
    print "====================================================================\n"
    if erro != "":
        print " * %s\n" % erro
        erro = ""

while (True):
    Cabecalho()
    print " | Menu:"
    print ' +--------------------------------------------------------->\n'
    print " [C/c] Coletar Dados"
    print " [S/s] Sair"
    opc = raw_input("\n >")

    if opc.upper() == 'C':
        opc = "i"
        while (opc not in 'RrDdCc' or opc == ""):
            Cabecalho()
            print " | Menu > Coletar Dados:"
            print ' +--------------------------------------------------------->\n'
            print " [R/r] Dados Brutos ou Rol"
            print " [D/d] Tabela Variável Dicreta (Sem intervalo de Classes)"
            print " [C/c] Tabela Variável Continua (Com intervalo de Classes)"
            opc = raw_input("\n >")
            if opc.upper() == "R":
                # r é uma instancia de Rol
                r = CreateRol()
                rol = Rol(r)
                dados = Dados(rol)
            elif opc.upper() == "D":
                TabelaDiscreta()
            elif opc.upper() == "C":
                TabelaContinua()
            else:
                erro = "Escolha uma opção Válida!"
        while(True):
            Cabecalho()
            print " | Menu > Coletar Dados > Apresentar:"
            print ' +--------------------------------------------------------->\n'
            print " [R/r] Apresentar Rol Ordenado (Nem sempre Disponivel)"
            print " [T/t] Apresentar Tabela"
            print " [C/c] Medidas de Tendencia Central"
            print " [D/d] Medidas de Dispersao"
            print " [E/e] Editar Rol"
            print " [V/v] Voltar ao Menu principal:"
            opc = raw_input("\n >")
            if opc.upper() == "R":
                CabecalhoMini()
                dados.Rol.Imprimir()
                raw_input("\n\n\n\n\n\n\n\n\n\nPressione 'Enter' para voltar...")
                pass
            elif opc.upper() == "T":
                dados.Tabela.Imprimir()
                pass
            elif opc.upper() == "C":
                print "Não implementado"
                pass
            elif opc.upper() == "D":
                print " [A/a] Amostra"
                print " [P/p] População"
            elif opc.upper() == "E":
                print "Não implementado"
                pass 
            elif opc.upper() == "V":
                opc = "i"
                while (opc not in "SsNn"):
                    CabecalhoMini()
                    print "Tem certeza que deseja voltar ao menu? (S/n)"
                    print "(Os dados serão perdidos)"
                    opc = raw_input("\n >")
                if opc.upper() == "S":
                    system(limpar)
                    break
                elif opc.upper() == "N":
                    pass
    
    #Sair do Maluest
    elif opc.upper() == 'S':
        opc = "i"
        while(opc not in "SsNn"):
            CabecalhoMini()
            print "Sair do Maluest? (S/n)"
            opc = raw_input("\n >")
        if opc.upper() == 'S':
            system(limpar)
            break
        elif opc.upper() == 'N':
            pass

'''    if opc.upper() == 'D':
        CreateRol()
        r = Rol(Rol)
        print 'Os dados ordenados ficaram assim:\n'
        print r.Imprimir()
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
        break'''
