""" Primeiro trabalho de Inteligência Artificial
    Aluna    :  Lorena Bacheti Bassani
    Tema     :  Algoritmos de Busca
    Trabalho :  O primeiro trabalho será uma atividade de avaliação dos algoritmos implementados em laboratório 
                    para o problema da mochila.
               Este trabalho consiste em realizar uma comparação experimental entre um conjunto pré-definido de 
                    metaheurísticas aplicadas ao problema da mochila. As metaheurísticas escolhidas são: Hill Climbing, 
                    Beam Search, Simulated Annealing, Genetic Algorithm e GRASP.

    Primeira Prova de Inteligência Artificial
    Aluna   :   Lorena Bacheti Bassani
    Tema    :   Algoritmos de Busca
    Estudos :   Algoritmos de Busca Baseada em soluções parciais, busca local e busca populacional.
                A matéria estudada é:
                    Algoritmos de Busca Baseados em soluções parciais
                        * Hill Climbing
                        * Beam Search
                        * Branch and Bound
                        * A*
                    Algoritmos de Busca Baseados em soluções completas -> Busca Local
                        * Simple Descent
                        * Deepest Descent
                        * Multistart Descent
                        * Simulated Annealing
                        * GRASP
                        * Tabu Search
                    Algoritmos de Busca Baseados em soluções completas -> Busca Populacional
                        * Algoritmo Genético
                        * Colonia de Formigas
                        * Enxame de Partículas
"""
from Busca.ProblemasBusca.mochila import mochila
from Busca.AlgoritmosBusca.hillClimbing import hillClimbing
from Busca.AlgoritmosBusca.beamSearch import beamSearch
from Busca.AlgoritmosBusca.simulatedAnnealing import simulatedAnnealing
from Busca.AlgoritmosBusca.genetico import algoritmoGenetico
from Busca.AlgoritmosBusca.grasp import grasp
from ioTools import resultadosFileReader
from problemas import problemasTeste, problemasTreino
import pandas as pd
import trabalhoIA

# Leitura dos Resultados do Treinamento
resultadosTreinamentos = { }

graspReader = resultadosFileReader("resultadoTreinamentoGRASP.result")
resultadosTreinamentos["GRASP"] = graspReader.read()

simulatedAnnealingReader = resultadosFileReader("resultadoTreinamentoSimulated Annealing.result")
resultadosTreinamentos["Simulated Annealing"] = simulatedAnnealingReader.read()

beamSearchReader = resultadosFileReader("resultadoTreinamentoBeam Search.result")
resultadosTreinamentos["Beam Search"] = beamSearchReader.read()

geneticoReader = resultadosFileReader("resultadoTreinamentoAlgoritmo Genetico.result")
resultadosTreinamentos["Algoritmo Genetico"] = geneticoReader.read()

# Leitura dos arquivos de resultados
resultadosTestes = { }

hillClimbingReader = resultadosFileReader("resultadoFinalHill Climbing.result")
resultadosTestes["Hill Climbing"] = hillClimbingReader.read()

graspReader = resultadosFileReader("resultadoFinalGRASP.result")
resultadosTestes["GRASP"] = graspReader.read()

simulatedAnnealingReader = resultadosFileReader("resultadoFinalSimulated Annealing.result")
resultadosTestes["Simulated Annealing"] = simulatedAnnealingReader.read()

beamSearchReader = resultadosFileReader("resultadoFinalBeam Search.result")
resultadosTestes["Beam Search"] = beamSearchReader.read()

geneticoReader = resultadosFileReader("resultadoFinalAlgoritmo Genetico.result")
resultadosTestes["Algoritmo Genetico"] = geneticoReader.read()

# Cria dicionário de resultados por problema
resultadosProblemas = { }
normalizadoPorProblemaTeste = {}
for prob, _ in problemasTeste.items():
    resultadosProblemas[prob] = {}
    for algoritmo, valor in resultadosTestes.items():
        valor = valor[0]
        aux = list(filter(lambda x: x["Problema"][0] == prob, valor))
        valor = list(map(lambda x: x["Resultados"], aux))
        resultadosProblemas[prob][algoritmo] = valor[0]
    normalizadoPorProblemaTeste[prob] = {}
    aux = list(map(lambda x: x[1]["Resposta"][1], resultadosProblemas[prob].items()))
    mini, maxi = min(aux), max(aux)
    divisor = maxi - mini
    for algoritmo, valor in resultadosProblemas[prob].items():
        normalizadoPorProblemaTeste[prob][algoritmo] = (valor["Resposta"][1] - mini)/divisor

normalizadoPorHeuristica = {
    "Hill Climbing" : list(),
    "Beam Search" : list(),
    "Simulated Annealing" : list(),
    "GRASP" : list(),
    "Algoritmo Genetico" : list()
}
for prob, valor in normalizadoPorProblemaTeste.items():
    for meta, resul in valor.items():
        normalizadoPorHeuristica[meta].append(resul)

# Obter média e descio padrão dos resultados normalizados de cada metaheurística
meanstdNormalizadas = { }
for al, valor in normalizadoPorHeuristica.items():
    aux = pd.Series(valor)
    meanstdNormalizadas[al] = (aux.mean(), aux.std())

resultadosPorHeuristica = { }
for al, valor in resultadosTestes.items():
    valor = valor[0]
    resultadosPorHeuristica[al] = list()
    for v in valor:
        resultadosPorHeuristica[al].append(v["Resultados"]["Resposta"][1])

meanstdHeuristicas = { }
for al, valor in resultadosPorHeuristica.items():
    aux = pd.Series(valor)
    meanstdHeuristicas[al] = (aux.mean(), aux.std())

temposExecucao = { }
for al, valor in resultadosTestes.items():
    valor = valor[1]
    temposExecucao[al] = valor

meanstdTempos = { }
for al, valor in temposExecucao.items():
    aux = pd.Series(valor)
    meanstdTempos[al] = (aux.mean(), aux.std())
