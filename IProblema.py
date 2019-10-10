import random as r
import math as m

class TimedOutExc(Exception):
    pass

class IProblema:
    # descreve o problema
    def descricao(self):
        raise NotImplementedError

    # retorna a aptidão atual de um estado
    def aptidao(self, estado):
        raise NotImplementedError

    # diz se um estado é válido para a instância do problema
    def valido(self, estado):
        raise NotImplementedError

    # gera os vizinhos de um estado (gera apenas vizinhos "a frente" se todaVizinhanca = False)
    def gerarVizinhos(self, estado, todaVizinhanca = False):
        raise NotImplementedError

    # gerar um estado aleatório
    def estadoAleatorio(self):
        raise NotImplementedError

    # retorna o estado considerado nulo no problema
    def estadoNulo(self):
        raise NotImplementedError

    # retorna do nEstados melhores estados na lista de estados
    def escolheMelhores(self, estados, nEstados, validosOnly = True):
        valEstados = list(map(lambda x: (self.aptidao(x), estados.index(x)),estados))
        if validosOnly:
            valEstados = list(filter((lambda x: self.valido(estados[x[1]])),valEstados))
        valEstados.sort(reverse = True)

        if len(valEstados) > nEstados:
            valEstados = valEstados[:nEstados]
        
        novosEstados = []
        for i in valEstados:
            novosEstados.append(estados[i[1]])

        return novosEstados

    # retorna o melhor estado
    def melhorEstado(self, estados, validoOnly = True):
        aux = self.escolheMelhores(estados, 1, validoOnly)
        if aux:
            return aux[0]
    
        return []
    
    # retorna o resultado da busca caso metodo de busca tenha sido passado
    def busca(self, estado, metodoBusca = None, tempo = list(), **keyargs):
        if metodoBusca is None:
            raise NotImplementedError
        if keyargs:
            metodoBusca(self, estado, tempo = tempo, **keyargs)
        else:
            metodoBusca(self, estado, tempo)

class IProblemaGenetico(IProblema):
    
    # função de seleção de sobreviventes
    def selecao(self, estados):
        raise NotImplementedError

    # função de crossover
    def crossover(self, estado1, estado2):
        raise NotImplementedError

    # função de mutação
    def mutacao(self, estado):
        raise NotImplementedError

    # gera uma população a partir do primeiro individuo da população dada
    def gerarPopulacao(self, populacao, tamanhoPop):
        raise NotImplementedError

    # retorna o melhor estado de uma geração
    def melhorDaGeracao(self, estados):
        melhor = self.melhorEstado(estados)
        if melhor:
            return melhor
        return self.estadoNulo()

class IProblemaBranchAndBound(IProblema):

    # função de estimativa (pessimista por default)
    def estimativa(self, estado, otimista=False):
        raise NotImplementedError

class IProblemaSimulatedAnnealing(IProblema):

    # função que aceita ou não um vizinho de um estado
    def aceitarVizinho(self, estado, vizinho, t):
        if not self.valido(vizinho):
            return False
        elif self.melhorEstado([estado, vizinho]) == vizinho:
            return True
        else:
            valorViz = self.aptidao(vizinho)
            valorEst = self.aptidao(estado)
            p = 1/(m.exp((valorEst - valorViz)/t))
            p = p if p >= 0 else -p
            n = r.random()
            return n < p

class IProblemaGRASP(IProblema):

    # método de construção guloso
    def construcaoGulosa(self, estado, m, semente):
        melhor = self.estadoNulo()
        aux = melhor
        r.seed(semente)

        while len(aux) != 0 :
            melhor = aux
            aux = self.escolheMelhores(self.gerarVizinhos(melhor), m)

            if aux:
                aux = aux[r.randint(0,len(aux)-1)]

        estado.clear()
        estado.extend(melhor)

    def buscaLocal(self, estado, metodoBuscaLocal, **keyargs):
        self.busca(estado, metodoBusca= metodoBuscaLocal, **keyargs)

class IProblemaDescida(IProblema):
    def escolheMelhoresDescent(self, estado, estados):
        resp = list(filter(lambda x: self.melhorEstado([x, estado] == x), estados))
        return resp
