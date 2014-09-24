#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system, name
from Malu import *

#variáveis globais
erro = ""
dados = None
rol = None

if name.upper() == "NT":
    limpar = "cls"
else:
    limpar = "clear"


def CreateRol():
    Rol = []
    CabecalhoMini()
    try:
        lenRol = int(raw_input(' Tamanho da coleção: > '))
    except:
        lenRol = 0
    if lenRol == 0:
        lenRol = 100000
    print " .Leitura dos dados:"
    for i in range(lenRol):
        try:
            Rol.append(int(raw_input('%4d > ' %(i+1))))
        except:
            break
    return Rol

def TabelaDiscreta():
    global erro
    K = 0
    while K < 1:
        CabecalhoMini()
        print ' Quantos Dados (linhas) tem nossa tabela?'
        K = int(raw_input("\n >"))
        if K < 1:
            erro = "Ops.. não acredito que ela tenha " + str(K) + " linhas! Tente de novo!"

    CabecalhoMini()
    print ' Perfeito! Agora para terminar, me passeos x(i) e as frequencias (fi):'
    print '  ~Comece pela primeira linha, e continue em ordem ate a ultima!'
    print '  ~Digite um numero e pressione Enter:\n\n'
    fi = []
    xi =[]
    for i in range(K):
        n = ''
        while n.__class__ != int:
            n = raw_input( "xi da " + str(i + 1) + "º linha: ")
            try:
                n = int(n)
                xi.append(n)
            except:
                print "\n\n * Ops.. o xi deve ser um Numero!"
        n = ''
        while n.__class__ != int:
            n = raw_input( "f(i) da " + str(i + 1) + "º linha: ")
            try:
                n = int(n)
                fi.append(n)
            except:
                print "\n\n * Ops.. o xi deve ser um Numero!"
    parametros = [K, xi, fi]
    return parametros

def TabelaContinua():
    global erro
    K = 0
    while K < 1:
        CabecalhoMini()
        print ' Quantas Classes (linhas) tem nossa tabela?'
        K = int(raw_input("\n >"))
        if K < 1:
            erro = "Ops.. não acredito que ela tenha " + str(K) + " linhas! Tente de novo!"

    CabecalhoMini()
    print ' Certo! E qual o Intervalo INFERIOR da PRIMEIRA Classe (linha)?'
    print ' (Ex ->   25 |--- 39  -> Neste caso seria 25)'
    I = int(raw_input("\n >"))

    S = 0
    while S <= I:
        CabecalhoMini()
        print ' Muito Bem! E o intervalo SUPERIOR da ULTIMA Classe (Linha)?'
        print ' (Ex ->   87 |--- 99  -> Neste caso seria 99)'
        S = int(raw_input("\n >"))
        if S <= I:
            erro = "Ops.. seu Intervalo Superior deve ser Maior que '" + str(I) + "' (Inferior)!"

    CabecalhoMini()
    print ' Perfeito! Agora para terminar, me passe as frequencias (fi):'
    print '  ~Comece pela primeira linha, e continue em ordem ate a ultima!'
    print '  ~Digite um numero e pressione Enter:\n\n'
    fi = []
    for i in range(K):
        n = ''
        while n.__class__ != int:
            n = raw_input( str(i + 1) + "º linha: ")
            try:
                n = int(n)
                fi.append(n)
            except:
                print "\n\n * Ops.. o intervalo deve ser um Numero!"
    parametros = [K, I, S, fi]
    return parametros


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
                p = TabelaDiscreta()
                dados = Dados()
                dados.LerTabelaD(p[0], p[1], p[2])
            elif opc.upper() == "C":
                p = TabelaContinua()
                dados = Dados()
                dados.LerTabelaC(p[0], p[1], p[2], p[3])
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
                if rol == None:
                    erro = "Ops.. acho que não temos um rol para te mostrar!"
                CabecalhoMini()
                if rol != None:
                    dados.Rol.Imprimir()
                raw_input("\n\n\nPressione 'Enter' para voltar...")
                pass
            elif opc.upper() == "T":
                if dados == None:
                    erro = "Ops.. acho que não temos uma tabela para te mostar!"
                CabecalhoMini()
                if dados != None:
                    dados.Tabela.Imprimir()
                raw_input("\n\n\nPressione 'Enter' para voltar...")
                pass
            elif opc.upper() == "C":
                if dados == None:
                    erro = "Ops.. acho que não temos esses dados para te mostar!"
                CabecalhoMini()
                if dados != None:
                    dados.TendenciaCentral.Imprimir()
                raw_input("\n\n\nPressione 'Enter' para voltar...")
                pass
            elif opc.upper() == "D":
                opc = 'i'
                while opc not in 'AaPp':
                    print " Qual o tipo da coleta?"
                    print " [A/a] Amostra"
                    print " [P/p] População"
                    opc = raw_input("\n >")
                CabecalhoMini()
                if opc.upper() == "A":
                    opc = "Amostra"
                elif opc.upper() == "P":
                    opc = "Populacao"
                dados.tipo = opc
                dados.Dispercao.Imprimir()
                raw_input("\n\n\nPressione 'Enter' para voltar...")
            elif opc.upper() == "E":
                erro = "Não implementado"
                CabecalhoMini()
                raw_input("\n\n\nPressione 'Enter' para voltar...")
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
                    del(dados)
                    dados = None
                    del(rol)
                    rol = None
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

    else:
        erro = "Digite uma opção válida!"
