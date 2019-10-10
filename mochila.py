import random as r
import math as m
import IProblema as interface

class mochila(interface.IProblemaBranchAndBound, interface.IProblemaDescida, interface.IProblemaGRASP, interface.IProblemaSimulatedAnnealing, interface.IProblemaGenetico, interface.IProblema):

    def __init__(self, valores, maxTam):
        # valores da mochila: O valor do elemento está em 0 e o volume em 1
        self.valores = valores
        self.maxTam = maxTam

    # descreve o problema
    def descricao(self):
        return tuple((self.valores, self.maxTam))

    # retorna valor atual de um estado
    def valorAtual(self, estado):
        valor = 0

        for i in range(0, len(estado)):
            valor = valor + estado[i]*self.valores[i][0]

        return valor

    # retorna tamanho atual de um estado
    def tamanhoAtual(self, estado):
        tamanho = 0

        for i in range(0, len(estado)):
            tamanho = tamanho + estado[i]*self.valores[i][1]

        return tamanho

    # retorna a aptidão atual de um estado
    def aptidao(self, estado):
        return self.valorAtual(estado)

    # diz se um estado é válido para a instância do problema
    def valido(self, estado):
        tamanho = self.tamanhoAtual(estado)
        return tamanho <= self.maxTam and tamanho >= 0

    # gera os próximos estados a partir do atual
    def gerarVizinhos(self, estado, todaVizinhanca = False):
        proximos = []

        for i in range(0, len(estado)):
            novoEstado1 = estado.copy()
            novoEstado1[i] = novoEstado1[i] + 1
            proximos.append(novoEstado1)
            if todaVizinhanca:
                novoEstado2 = estado.copy()
                novoEstado2[i] = novoEstado2[i] - 1
                if novoEstado2[i] > 0:
                    proximos.append(novoEstado2)
            
        return proximos

    # gerar um estado aleatório
    def estadoAleatorio(self):
        estado = [0]*len(self.valores)
        resp = estado.copy()
        indexList = list(range(len(self.valores)))

        for _ in range(0, len(self.valores)):
            i = r.choice(indexList)
            indexList.remove(i)
            estado[i] = (r.randint(0, m.ceil((self.maxTam-1)/self.valores[i][1])))
            if not self.valido(estado):
                break
            else:
                resp = estado.copy()
        return resp

    # função de crossover em ponto único (troca de partes entre estados)
    def crossover(self, estado1, estado2):
        # numero de crossovers
        i = r.randint(0, len(estado1) - 1)
        for _ in range(0, i):
            # posições de crossover
            k = r.randint(0, len(estado1) - 1)
            j = r.randint(0, len(estado2) - 1)
            aux = estado1[k]
            estado1[k] = estado2[j]
            estado2[j] = aux

    # função de mutação (aleatoriamente muda uma parte do estado)
    def mutacao(self, estado):
        # numero de mutações (máximo 20)
        i = r.randint(0, ((len(estado) - 1) % 21))
        for _ in range(0, i):
            q = -1 + 2*r.randint(0, 1)
            k = r.randint(0, len(estado) - 1)
            if estado[k] + q >= 0:
                estado[k] = estado[k] + q

    # função de seleção por roleta (mantem um sobrevivente na população)
    def selecao(self, estados):
        """ primeiro passo : definir as faixas de sobrevivência
                Como :  calcular as probabilidades de cada um sobreviver (aptidao/sum(aptidoes))
                        calcular a faixa de sobrevivência
        """
        total = sum(list(map(lambda x: self.aptidao(x), estados)))
        porcentagens = list(map(lambda x: (x, self.aptidao(x)/total),estados))

        faixaSobrevivencia = list()
        limiteInf = 0
        for e in porcentagens:
            faixaSobrevivencia.append((limiteInf, limiteInf + e[1], e[0]))
            limiteInf = limiteInf + e[1]
        
        """ segundo passo : escolher o sobrevivente 
                Como :  gerar um número aleatório
                        descobrir em qual faixa de sobrevivência ele se encontra
        """
        n = r.uniform(0,1)
        for e in faixaSobrevivencia:
            if n >= e[0] and n < e[1]:
                estados.clear()
                estados.append(e[2])
        

    # gera uma população a partir do primeiro individuo da população dada
    def gerarPopulacao(self, populacao, tamanhoPop):
        acrescer = tamanhoPop - len(populacao)
        estado = populacao[0]
        while len(populacao) < tamanhoPop:
            for i in range(0, len(estado)):
                if i >= acrescer:
                    break
                novoEstado = estado.copy()
                novoEstado[i] = novoEstado[i] + -1 + 2*r.randint(0, 1)
                if novoEstado[i] > 0:
                    populacao.append(novoEstado)

    # retorna o estado considerado nulo no problema
    def estadoNulo(self):
        return [0]*len(self.valores)
    
    def estimativa(self, estado, otimista):
        previsto = estado.copy()
        melhorValor = (1,0)
        for i in self.valores:
            if i[1]/i[0] > melhorValor[1]/melhorValor[0]:
                melhorValor = i
        while True:
            proxEstado = previsto
            proxEstado[self.valores.index(melhorValor)] = proxEstado[self.valores.index(melhorValor)] + 1
            if not self.valido(proxEstado):
                break
            previsto = proxEstado
        
        if otimista:
            previsto[self.valores.index(melhorValor)] = previsto[self.valores.index(melhorValor)] + 1

        return previsto

""" Testes para a mochila:
    print(m.estadoNulo(), m.estadoAleatorio())
    pop = [[1,2,3]]
    m.gerarPopulacao(pop,3)
    print(pop)
    print(m.selecao(pop))
    m.mutacao(pop[0])
    print(pop)
    m.crossover(pop[1],pop[2])
    print(pop)
    print(m.gerarVizinhos(pop[0], True))
    print(pop[2],m.valido(pop[2]))
    print([-1,0,0], m.valido([-1,0,0]))
    print(m.estadoNulo(),m.valido(m.estadoNulo()))
    print([1,0,2], m.valido([1,0,2]))
    print([0,2,1],m.valido([0,2,1]))
    print([0,2,1], m.aptidao([0,2,1])) """