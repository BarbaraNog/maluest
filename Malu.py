#! usr/bin/env python
#-*- coding: utf-8 -*-

from math import sqrt

class Rol(object):
	def __init__(self, Rol = []):
		self.Rol = Rol
		self.Ordenar()
		self.Len = len(self.Rol)

	#Vai para a view
	def Imprimir(self):
		indice = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'
		num = 0
		taux = (indice[num],)
		val = ' %5d |'
		vazio = '       |'
		_print = ' %s |'
		_linha = '---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+'
		print '   |   I   |   II  |  III  |   IV  |   V   |   VI  |  VII  |  VIII |   IX  |   X   |'
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

	def Inserir(self, Rol):
		self.__init__(Rol)

	def Ordenar(self):
		self.Rol.sort()
	
	def Alterar(self, posicao, valor):
		if posicao < self.Len:
			self.Rol[posicao -1] = valor
			return True
		else:
			return False
	
	def Remover(self, posicao):
		if posicao < self.Len:
			self.Rol.__delitem__(posicao -1)
			self.Len = len(self.Len)
			return True
		else:
			return False

	def Adicionar(self, valor):
		self.Rol.append(valor)
		self.Len = len(self.Len)
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

	#get e set de Amplitude
	def _get_At(self):
		return (self.Rol.Rol[-1] - self.Rol.Rol[0]) + self._At
	def _set_At(self, at):
		self._At = at - (self.Rol.Rol[-1] - self.Rol.Rol[0])
	At = property(_get_At, _set_At)
	
	#get e set do Numero de Classes
	def _get_K(self):
		return int(sqrt(len(self.Rol.Rol))) + self._K
	def _set_K(self, k):
		if int(sqrt(len(self.Rol.Rol)))-1 <= k <= int(sqrt(len(self.Rol.Rol)))+1:
			self._K = k - int(sqrt(len(self.Rol.Rol)))	
	K = property(_get_K, _set_K)


	#get e set do intervalo de classes
	@property
	def Ik(self):
		if self.At % self.K == 0:
			return self.At / self.K
		else:
			self.At +=1
			self.Ik
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
		self.Rol = dados.Rol
		self.K = dados.K
		self.Ik = dados.Ik
		self.variavel = 0
		self.tabela = []

	def Imprirmir(self):
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
                for i in self.Rol.Rol:
                        if i not in aux:
                                aux.append(i)
                F = 0
                _F = 0.0
                print '  x(i)  |   fi   |   fr %   |   F   |    F %'
                print '--------+--------+----------+-------+-----------'
                for i in aux: 
                        F += self.Rol.Rol.count(i)
                        _F += float(self.Rol.Rol.count(i))/float(self.lenRol) * 100
                        print ('  %4d  |  %4d  |  %6.3f  |  %3d  |  %7.3f') % (i, self.Rol.Rol.count(i),  float(self.Rol.Rol.count(i))/float(self.lenRol) * 100, F, _F)

	def DetectarVariavel(self):
		'''
		Não foram encontradas referencias em literaturas
		para esse fim.
		'''
		laux = []
		for i in self.Rol.Rol:
			if i not in laux:
				laux.append(i)
		if len(laux) > 10:
			#Variavel Quantitativa Contínua
			self.variavel = 1
		elif (float(len(self.Rol.Rol)) / float(len(laux))) < 2:
			self.variavel = 1
		else:
			#Variável Quantitativa Discreta
			self.variavel = 2

	def ClassificaDados(self):
		self.tabela = []
		for i in range(self.K):
			self.tabela.append({})
			self.tabela[-1]['K'] = i + 1
			self.tabela[-1]['I'] = self.Rol.Rol[0] + (self.Ik * i)
			self.tabela[-1]['S'] = self.tabela[-1]['I'] + self.Ik
			self.tabela[-1]['fi'] = self.Frequencia(self.tabela[-1]['I'], self.tabela[-1]['S'])
			self.tabela[-1]['fir'] = (float(self.tabela[-1]['fi']) / float(len(self.Rol.Rol))) * 100
			self.tabela[-1]['xi'] = float(self.tabela[-1]['I'] + self.tabela[-1]['S'])/2.0
			self.tabela[-1]['xifi'] = self.tabela[-1]['xi'] * self.tabela[-1]['fi']
			self.tabela[-1]['F'] = 0
			for i in self.tabela:
				self.tabela[-1]['F'] += i['fi']
			self.tabela[-1]['Fr'] = (float(self.tabela[-1]['F']) / float(len(self.Rol.Rol))) * 100 
	
	def Frequencia(self, I, S):
		aux = 0;
		for i in self.Rol.Rol:
			if S > i >= I:
				aux += 1
		return aux



class MedidaTendenciaCentral(object):
	def __init__(self, dados):
		self.media = 0
		self.mediana = 0
		self.moda = {'Czuber' : [], 'Pearson' : [], 'King' : [], 'Convencional' : []}
		self.Tabela = dados.Tabela
		self.tabela = dados.Tabela.tabela
		self.Rol = dados.Rol
	
	def __repr__(self):
		return 'Medidas de Tendencia Central'

	def _get_moda(self):
		return "{'Czuber' : ", moda["Czuber"], ", 'Pearson' : ", moda["Pearson"],", 'King' : ", moda["King"], ", 'Convencional' : ", moda["Convencional"],"}"

	def Media(self):
		'''
		O Mesmo para Contínua e Discreta
		'''
		Sfi = 0
		Sxifi = 0
		for i in self.tabela:
			Sfi += i['fi']
			Sxifi += i['xifi']
		self.media = float(Sxifi)/float(Sfi) 
	
	def Mediana(self):
		if self.Tabela == 1: #Discreta
			if self.Rol.Len % 2 == 1:
				self.mediana = self.Rol.Rol[(self.Rol.Len / 2) + 1]
			else:
				self.mediana = (float(self.Rol.Rol[self.Rol.Len / 2] + self.Rol.Rol[(self.Rol.Len / 2) + 1]) / 2.0)
		else: #Continua
			posicao = float(len(self.Rol.Rol))/2.0
			for i in self.tabela:
				if posicao <= i['F']:
					linha = i['K']
					break
			Fant = 0
			if linha != 1:
				Fant = self.tabela[linha - 2]['F']
			I = float(self.tabela[linha - 1]['I'])
			fimd = float(self.tabela[linha - 1]['fi'])
			Ik = self.Tabela.Ik
			Md = I + (((posicao - Fant)/fimd)*Ik)
			self.mediana = Md
	
	'''
	O Metodo Moda, calcula a Moda do Rol, ou seja, o elemento de maior frequência.
	Encontra a linha modal (linha com maior Frequencia 'fi') e realiza as operações!
	São quatro métodos diferentes para se encontrar a Moda de uma amostra/população.
	No Metodo Convencional, a moda é igual ao 'xi' da classe modal.
	No metodo de King, a moda segue a formula (Mo = I + (((Fant)/Fant + Fpos) * Ik))
	'''
	def Moda(self):
		''' Os valores da Media e da Mediana serão necessários para cauculo da Moda de Pearson'''
		self.Media()
		self.Mediana()
		
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
			pearson = ((3 * self.mediana) - (2 * self.media))
			self.moda['Pearson'].append(pearson)
		
			'''Método de King'''
			king = (j[k]['I'] + ((float(j[k + 1]['fi'])/float(j[k + 1]['fi'] + j[k - 1]['fi'])) * self.Ik))
			self.moda['King'].append(king)
			
			'''Método Czuber'''
			czuber = (j[k]['I'] + ((float(j[k]['fi'] + j[k - 1]['fi'])/float((2 * j[k]['fi']) - j[k -1]['fi'] - j[k + 1]['fi'])) * self.Ik))
			self.moda['Czuber'].append(czuber)


class MedidaDeDispercao(object):
	def __init__(self, dados, tipo):
		self.tipo = tipo
		self.tabela = dados.tabela.tabela
		self.media = dados.dispercao.media

	@property
	def variancia(self):
		soma = 0
		n = 0
		for i in self.tabela:
			soma += pow(i['xi'] - self.media, 2) * i['fi']
			n += i['fi']
		if self.tipo == "Amostra":
			n -+ 1;
		return float(soma) / float(n)

	@property
	def dp(self):
		return sqrt(self.variancia)

	@property
	def cv(self):
		return 100 * float(self.dp)/float(self.media)


if __name__ == '__main__':
	main()
