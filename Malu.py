#! usr/bin/env python
#-*- coding: utf-8 -*-

from math import sqrt
from random import randint

class Rol(object):
    def __init__(self, Rol = None):
        self.Rol = Rol
        if self.Rol != None:
            self.Ordenar()
        self._len = 0
    
    def _get_Len(self):
        if self.Rol != None:
            return len(self.Rol)
        else:
            return self._len
        def _set_Len(self, _len):
            if self.Rol == None:
                self._len = _len
        Len = property(_get_Len, _set_Len)

    #Vai para a view
    def Imprimir(self):
        indice = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'
        num = 0
        taux = (indice[num],)
        val = ' %4d |'
        vazio = '      |'
        _print = ' %s |'
        _linha = '---+------+------+------+------+------+------+------+------+------+------+'
        print '   |  I   |  II  | III  |  IV  |  V   |  VI  | VII  | VIII |  IX  |  X   |'
        print _linha
        for i in self.Rol:
            if len(taux) < 11:
                _print += val
                taux += (i,)
            else:
                num += 1
                print _print % taux
                print _linha
                _print = ' %s |'
                taux = (indice[num], )
                _print += val
                taux += (i,)
        if len(taux) > 0:
            for i in range(len(taux), 11):
                _print += vazio
            print _print % taux
            print _linha    

    def SubstituirRol(self, Rol):
        self.__init__(Rol)

    def Inserir(self, Rol):
            self.Rol.extend(Rol)

    def Ordenar(self):
        self.Rol.sort()
    
    def Alterar(self, antigo, novo):
        if antingo in self.Rol:
            self.Rol[self.Rol.index(antigo)] = novo
            return True
        else:
            return False
    
    def Remover(self, antigo):
        if antigo in self.Rol:
            self.Rol.__delitem__(self.Rol.index(antigo))
            return True
        else:
            return False

    def Adicionar(self, valor):
        self.Rol.append(valor)
'''
implementar:
    auto detctar o tipo da variável (Discreta ou Contínua)
    implementar modas de Person, Czuber e King
'''
class Dados(object):
    '''
    Rol é uma coleção de dados
    '''
    def __init__(self, Rol = Rol()):
        self.Rol = Rol
        self._K = 0  #incremento ou decremento para o Numero de Clases
        self._At = 1 #incremento da Amplitude
        self.tabela = None
        self.tendenciaCentral = None
        self.dispercao = None
        self.tipo = "Amostra"

    #get e set de Amplitude
    def _get_At(self):
        return (self.Rol.Rol[-1] - self.Rol.Rol[0]) + self._At
    def _set_At(self, at):
        self._At = at - (self.Rol.Rol[-1] - self.Rol.Rol[0])
    At = property(_get_At, _set_At)
    
    #get e set do Numero de Classes
    def _get_K(self):
        return int(sqrt(self.Rol.Len)) + self._K
    def _set_K(self, k):
        if int(sqrt(self.Rol.Len))-1 <= k <= int(sqrt(self.Rol.Len))+1:
            self._K = k - int(sqrt(self.Rol.Len))    
    K = property(_get_K, _set_K)


    #get e set do intervalo de classes
    @property
    def Ik(self):
        while self.At % self.K != 0:
            self.At += 1
        if self.At % self.K == 0:
            return self.At / self.K
        
        def LerTabelaD(self, K, xi = [], fi = []):
            if len(fi) > 0 and len(xi) == len(fi):
                self.Rol.Rol = []
                for i in fi:
                    for j in range(i):
                        self.Rol.Rol.append(i)
                self.Rol.Ordenar()

    def LerTabelaC(self, K, I, S, fi = []):
        if len(fi) > 0:
            At = S-I
            Ik = At/K
            i = I
            self.Rol.Rol = []
            for k in fi:
                self.Rol.Rol.append(i)
                i += Ik
            i = I
            for k in fi:
                for j in range(k-1):
                    #O randint é só pra dar um charme =D
                    self.Rol.Rol.append(randint(i, i+Ik-1))
                i += Ik
            self.Rol.Ordenar()
            self.At = At
            self.K = K

    @property    
    def Tabela(self):
        if self.tabela == None:
            self.tabela = Tabela(self)
        return self.tabela
    
    @property
    def TendenciaCentral(self):
        if self.tendenciaCentral == None:
            self.tendenciaCentral = MedidaTendenciaCentral(self)
        return self.tendenciaCentral

    @property
    def Dispercao(self):
        if self.dispercao == None:
            self.dispercao = MedidaDeDispercao(self)
        return self.dispercao

class Tabela(object):
    def __init__(self, dados):
        self.dados = dados
        self.variavel = None
        self._tabela = []

        @property
        def tabela(self):
                self.ClassificaDados()
                return self._tabela

    def Imprimir(self):
        if self.variavel == None:
            self.DetectarVariavel()
        if self.variavel == 1:
            self.Continua()
        elif self.variavel == 2:
            self.Discreta()
        else:
            print 'Ops.. não conseguimos identificar se essa variável é Discreta ou Contínua'
        
    def Continua(self):
        print '  Cls  |  Int. Classes  |   fi   |   fr %   |   F   |    F %    |   xi   |   xi X fi'
        print '-------+----------------+--------+----------+-------+-----------+--------+----------'
        for i in self.tabela:
            tupla = (i['K'], i['I'], i['S'], i['fi'], i['fir'], i['F'], i['Fr'], i['xi'], i['xifi'])
            print ('  %3d  |  %4d |- %4d  |  %4d  |  %6.3f  |  %3d  |  %7.3f  | %6.2f | %9.2f ') % tupla 
    
    def Discreta(self):
        aux = []
        for i in self.dados.Rol.Rol:
            if i not in aux:
                    aux.append(i)
        F = 0
        _F = 0.0
        print '  x(i)  |   fi   |   fr %   |   F   |    F %    |   xi X fi'
        print '--------+--------+----------+-------+-----------+----------'
        for i in aux: 
            tupla = (i['xi'], i['fi'], i['fr'], i['F'], i['Fr'], i['xifi'])
            print ('  %4d  |  %4d  |  %6.3f  |  %3d  |  %7.3f  | %9.2f ') % tupla

    def DetectarVariavel(self):
        laux = []
        for i in self.dados.Rol.Rol:
            if i not in laux:
                laux.append(i)
        if len(laux) > 10:
            self.variavel = 1
        elif (float(len(self.dados.Rol.Rol)) / float(len(laux))) < 2:
            self.variavel = 1
        else:
            self.variavel = 2

    def ClassificaDados(self):
        self._tabela = []
        for i in range(self.dados.K):
            self._tabela.append({})
            self._tabela[-1]['K'] = i + 1
            self._tabela[-1]['I'] = self.dados.Rol.Rol[0] + (self.dados.Ik * i)
            self._tabela[-1]['S'] = self._tabela[-1]['I'] + self.dados.Ik
            self._tabela[-1]['fi'] = self.Frequencia(self._tabela[-1]['I'], self._tabela[-1]['S'])
            self._tabela[-1]['fir'] = (float(self._tabela[-1]['fi']) / float(len(self.dados.Rol.Rol))) * 100
            self._tabela[-1]['xi'] = float(self._tabela[-1]['I'] + self._tabela[-1]['S'])/2.0
            self._tabela[-1]['xifi'] = self._tabela[-1]['xi'] * self._tabela[-1]['fi']
            self._tabela[-1]['F'] = 0
            for i in self._tabela:
                self._tabela[-1]['F'] += i['fi']
            self._tabela[-1]['Fr'] = (float(self._tabela[-1]['F']) / float(len(self.dados.Rol.Rol))) * 100 
    
    def Frequencia(self, I, S):
        aux = 0;
        for i in self.dados.Rol.Rol:
            if S > i >= I:
                aux += 1
        return aux



class MedidaTendenciaCentral(object):
    def __init__(self, dados):
        self.moda = {'Czuber' : [], 'Pearson' : [], 'King' : [], 'Convencional' : []}
        self.Dados = dados
        self.Tabela = dados.Tabela
        self.tabela = dados.Tabela.tabela
        self.Rol = dados.Rol
    
    def __repr__(self):
        return 'Medidas de Tendencia Central'

        def Imprimir(self):
            self.Moda()
            print "        +---------------------------------------------+"
            print "        +----->   Medida de Tendencia Central   <-----+"
            print "        +---------------------------------------------+"
            print "        |  -> Media:   %15.8f                |" % self.Media
            print "        |  -> Mediana: %15.8f                |" % self.Mediana
            print "        |  -> Moda(s):                                |"
            print "        |   | -> Convencional:                        |"
            for i in self.moda["Convencional"]:
                print "        |   |  |  ->   %15.8f                |" % i
            print "        |   | -> King:                                |"
            for i in self.moda["King"]:
                print "        |   |  |  ->   %15.8f                |" % i
           
            print "        |   | -> Pearson:                             |"
            for i in self.moda["Pearson"]:
                print "        |   |  |  ->   %15.8f                |" % i
          
            print "        |   | -> Czuber:                              |"
            for i in self.moda["Czuber"]:
                print "        |   |  |  ->   %15.8f                |" % i
            print "        +---------------------------------------------+"

    @property
    def Media(self):
        '''
        O Mesmo para Contínua e Discreta
        '''
        Sfi = 0
        Sxifi = 0
        for i in self.Dados.Tabela.tabela:
            Sfi += i['fi']
            Sxifi += i['xifi']
        return float(Sxifi)/float(Sfi) 
    
    @property
    def Mediana(self):
        if self.Tabela.variavel == 1: #Discreta
            if self.Dados.Rol.Len % 2 == 1:
                return self.Rol.Rol[(self.Rol.Len / 2) + 1]
            else:
                    return (float(self.Rol.Rol[self.Rol.Len / 2] + self.Rol.Rol[(self.Rol.Len / 2) + 1]) / 2.0)
        else: #Continua
            posicao = float(self.Rol.Len)/2.0
            for i in self.tabela:
                if posicao <= i['F']:
                    linha = i['K']
                    break
            Fant = 0
            if linha != 1:
                Fant = self.tabela[linha - 2]['F']
            I = float(self.tabela[linha - 1]['I'])
            fimd = float(self.tabela[linha - 1]['fi'])
            Ik = self.Dados.Ik
            Md = I + (((posicao - Fant)/fimd)*Ik)
            return Md
    
    '''
    O Metodo Moda, calcula a Moda do Rol, ou seja, o elemento de maior frequência.
    Encontra a linha modal (linha com maior Frequencia 'fi') e realiza as operações!
    São quatro métodos diferentes para se encontrar a Moda de uma amostra/população.
    No Metodo Convencional, a moda é igual ao 'xi' da classe modal.
    No metodo de King, a moda segue a formula (Mo = I + (((Fant)/Fant + Fpos) * Ik))
    '''
    def Moda(self):
        aux = 0
        linhaMo = 0
        linhas = []
        
        '''Procura a Linha Modal'''
        for i in self.tabela:
            if i['fi'] > aux:
                aux = i['fi']
                linhaMo = i['K']
        linhas.append(linhaMo)
        
        '''Verifica a amostra tem mais de uma moda'''
        for i in self.tabela:
            if i['K'] != linhaMo and i['fi'] == aux:
                linhas.append(i['K'])
        
        
        for i in linhas:
            j = self.tabela
            k = i - 1
            
            '''Metodo Convencional'''
            self.moda['Convencional'].append(j[k]['xi'])    
            
            '''Metodo Pearson'''
            pearson = ((3 * self.Mediana) - (2 * self.Media))
            self.moda['Pearson'].append(pearson)
        
            '''Método de King'''
            king = (j[k]['I'] + ((float(j[k + 1]['fi'])/float(j[k + 1]['fi'] + j[k - 1]['fi'])) * self.Dados.Ik))
            self.moda['King'].append(king)
            
            '''Método Czuber'''
            czuber = (j[k]['I'] + ((float(j[k]['fi'] + j[k - 1]['fi'])/float((2 * j[k]['fi']) - j[k -1]['fi'] - j[k + 1]['fi'])) * self.Dados.Ik))
            self.moda['Czuber'].append(czuber)


class MedidaDeDispercao(object):
    def __init__(self, dados):
        self.dados = dados
        self.tipo = dados.tipo
        self.tabela = dados.Tabela.tabela

    @property
    def variancia(self):
        soma = 0
        n = 0
        for i in self.dados.Tabela.tabela:
            soma += pow(i['xi'] - self.dados.TendenciaCentral.Media, 2) * i['fi']
            n += i['fi']
        if self.tipo == "Amostra":
            n -= 1;
        return float(soma) / float(n)

    @property
    def dp(self):
        return sqrt(self.variancia)

    @property
    def cv(self):
        return 100 * float(self.dp)/float(self.dados.TendenciaCentral.Media)

    def Imprimir(self):
        print "        +---------------------------------------------+"
        print "        +----->       Medidas de Dispesão       <-----+"
        print "        +---------------------------------------------+"
        print "        |  -> Variância:   %15.8f            |" % self.variancia
        print "        |  -> Desvio Padrão: %15.8f          |" % self.dp
        print "        |  -> Coefifiente de Variação: %15.8f|" % self.cv
        print "        +---------------------------------------------+"

if __name__ == '__main__':
    pass
    #main()
