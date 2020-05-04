
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
from ..ProblemasBusca import IProblema
import random
import threading
from time import time

def algoritmoGenetico(problema, estado, maxIter, tamanhoPop, maxSemMelhora, chanceCross, chanceMutacao, tempo = list()):

    # Rotina de tempo limite
    encerrou = list()
    encerrou.append([False])

    if tempo:
        
        def saida(encerrou):
        
                encerrou.clear()
                encerrou.extend([True])

        temporizador = threading.Timer(tempo[0]*60, saida, encerrou)
        temporizador.start()
    
    inicio = time()

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
    try:
        while iterador < maxIter and geracoesSemMelhora < maxSemMelhora:
            if encerrou[0][0]:
                raise IProblema.TimedOutExc

            # seleciona os melhores e gera nova população
            problema.selecao(populacao)
            problema.gerarPopulacao(populacao, tamanhoPop)
            
            # realiza um número aleatório de crossovers e mutações entre 0 e 5
            for _ in range(1, random.randint(2, 20)):
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

    except IProblema.TimedOutExc:
        raise
    else:
        if tempo:
            temporizador.cancel()
    finally:
        estado.clear()
        estado.extend(melhor)
        final = time()
        if tempo: 
            temporizador.join()
            tempo.clear()        
        tempo.append(final - inicio)
