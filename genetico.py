
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
import IProblema
import random

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
