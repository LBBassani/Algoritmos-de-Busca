""" Primeiro trabalho de Inteligência Artificial
    Aluna    :  Lorena Bacheti Bassani
    Tema     :  Algoritmos de Busca
    Trabalho :  O primeiro trabalho será uma atividade de avaliação dos algoritmos implementados em laboratório 
                    para o problema da mochila.
               Este trabalho consiste em realizar uma comparação experimental entre um conjunto pré-definido de 
                    metaheurísticas aplicadas ao problema da mochila. As metaheurísticas escolhidas são: Hill Climbing, 
                    Beam Search, Simulated Annealing, Genetic Algorithm e GRASP.
"""
from mochila import mochila
import random

""" Metodo Hill Climbing
        Classe : Baseada em Soluções Parciais
        Hiperparametros : Não tem
        Necessita de Estado Inicial : Não
"""
def hillClimbing(problema, estado):
    melhor = problema.estadoNulo()
    aux = problema.melhorEstado(problema.gerarVizinhos(melhor))

    while len(aux) != 0 :
        melhor = aux
        aux = problema.melhorEstado(problema.gerarVizinhos(melhor))

    estado.clear()
    estado.extend(melhor)

""" Metodo Beam Search
        Classe : Baseada em Soluções Parciais
        Hiperparametros : 
            nEstados : número de estados mantidos na expansão
        Necessita de Estado Inicial : Não
"""
def beamSearch(problema, estado, nEstados):
    estados = [problema.estadoNulo()]
    estados.extend(problema.gerarVizinhos(estados[0]))
    estados = problema.escolheMelhores(estados, nEstados)
    melhor = []

    while len(estados) > 0:
        melhor = estados[0]
        avaliar = estados.copy()
        for e in avaliar:
            estados.remove(e)
            estados.extend(problema.gerarVizinhos(e))
        estados = problema.escolheMelhores(estados, nEstados)
    estado.clear()
    estado.extend(melhor)
 
""" Metodo Simulated Annealing
        Classe : Baseada em Soluções Completas -> Busca Local
        Hiperparametros :
            t : temperatura inicial
            a : taxa de queda de temperatura
            minT : temperatura mínima (critério de parada)
            numIter : quantidade de iterações por temperatura
        Necessita de Estado Inicial : Sim
"""
def simulatedAnnealing(problema, estado, t, a, minT, numIter):
    melhorEstado = estado.copy()
    aux = estado.copy()
    while t > minT:
        viz = problema.gerarVizinhos(aux, todaVizinhanca = True)
        for _ in range(1, numIter):
            if len(viz) == 0:
                break
            vizinho = viz.pop(random.randint(0, len(viz)-1))
            if problema.aceitarVizinho(aux, vizinho, t):
                aux = vizinho
                viz = problema.gerarVizinhos(aux, todaVizinhanca = True)
                if problema.melhorEstado([aux, melhorEstado]) == aux:
                    melhorEstado = aux
        t = t*a
    estado.clear()
    estado.extend(melhorEstado)

""" Metodo Algoritmo Genético
        Classe : Baseada em Soluções Completas -> Busca Populacional -> Computação Evolutiva
        Hiperparametros : 
            maxIter : número máximo de iterações (critério de parada)
            tamanhoPop : tamanho da população
            maxSemMelhora : número máximo de iterações sem melhora de resposta (critério de parada)
            chanceCross : chance de ocorrer crossover
            chanceMutacao : chance de ocorrer mutação
        Necessita de Estado Inicial : Não
"""
def algoritmoGenetico(problema, estado, maxIter, tamanhoPop, maxSemMelhora, chanceCross, chanceMutacao):
    # FIXME Resultados completamente aletatórios e péssimos
    def ocorreEvento(chance):
        n = random.random()
        if n <= chance:
            return True
        return False

    melhor = problema.estadoNulo()
    populacao = [melhor]
    problema.gerarPopulacao(populacao, tamanhoPop)

    melhorAptidaoAtual = 0
    geracoesSemMelhora = 0
    iterador = 0

    while iterador < maxIter and geracoesSemMelhora < maxSemMelhora:
        # seleciona os melhores e gera nova população
        problema.selecao(populacao)
        problema.gerarPopulacao(populacao, tamanhoPop)
        
        # realiza um número aleatório de crossovers e mutações entre 0 e 5
        for _ in range(1, random.randint(2, 5)):
            # verifica se ocorre Crossover
            if ocorreEvento(chanceCross):
                n = 0
                k = 0
                while n == k:
                    n = random.randint(0, len(populacao) - 1)
                    k = random.randint(0, len(populacao) - 1)
                problema.crossover(populacao[n], populacao[k])

            # verifica se ocorre mutação
            if ocorreEvento(chanceMutacao):
                n = random.randint(0, len(populacao) - 1)
                problema.mutacao(populacao[n])

        # testa se houve melhora em comparação ao melhor estado conhecido
        if(melhorAptidaoAtual > problema.aptidao(problema.melhorDaGeracao(populacao))):
            geracoesSemMelhora = geracoesSemMelhora + 1

        else:
            melhor = problema.melhorDaGeracao(populacao)
            melhorAptidaoAtual = problema.aptidao(problema.melhorDaGeracao(populacao))
            geracoesSemMelhora = 0
            
        iterador = iterador + 1

    estado.clear()
    estado.extend(melhor)

""" Metodo GRASP (Greedy Randomized Adaptive Search)
        Classe : Baseada em Soluções Completas -> Busca Local
        Hiperparametros : 
            m : elementos para escolher no construtor guloso de estados
            numIter : número de iterações total do algoritmo (critério de parada)
        Necessita de Estado Inicial : Não
"""
def grasp(problema, estado, m, numIter, metodoBuscaLocal):

    melhor = problema.estadoNulo()
    for _ in range(0, numIter):
        novoEstado = problema.estadoNulo()
        problema.construcaoGulosa(novoEstado, m, random.randint(0, 100))
        problema.buscaLocal(novoEstado, metodoBuscaLocal[0], **metodoBuscaLocal[1])
        if problema.melhorEstado([melhor, novoEstado]):
            melhor = novoEstado
    
    estado.clear()
    estado.extend(melhor)

""" Testes dos algoritmos """
def teste():
    paramHC = None
    paramBS = {"nEstados" : 3}
    paramSA = {"t" : 50, "a" : 0.6, "minT" : 1, "numIter" : 3}
    paramAG = {"maxIter" : 10, "tamanhoPop" : 3, "maxSemMelhora" : 15, "chanceCross" : 0.5, "chanceMutacao" : 0.5}
    paramGP = {"m" : 3, "numIter" : 10, "metodoBuscaLocal" : [simulatedAnnealing, paramSA]}
    try:
        m = mochila([(1, 3), (4, 6), (5, 7)], 19)
        metodos = [[hillClimbing, paramHC], [beamSearch, paramBS] , [simulatedAnnealing, paramSA], [algoritmoGenetico, paramAG], [grasp, paramGP]]
        estado = list()
        for metodo in metodos:
            if metodo[1]:
                m.busca(estado, metodo[0], **metodo[1])
            else:
                m.busca(estado,metodo[0])
            print("Resultado do Teste com", metodo[0].__name__, ":",estado)
            estado = m.estadoNulo()
    except NotImplementedError:
        print("Algum método não está implementado")
    finally:
        print("Final do Teste :)")

teste()