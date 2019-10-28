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
from ioTools import resultadosFileReader
from problemas import problemasTeste, problemasTreino
import pandas as pd
import numpy as np
import seaborn as sea
from matplotlib import pyplot as plt
import trabalhoIA

import scriptTreinamento

# Leitura dos Resultados do Treinamento
resultadosTreinamentos = { }

graspReader = resultadosFileReader("Resultados/resultadoTreinamentoGRASP.result")
resultadosTreinamentos["GRASP"] = graspReader.read()

beamSearchReader = resultadosFileReader("Resultados/resultadoTreinamentoBeam Search.result")
resultadosTreinamentos["Beam Search"] = beamSearchReader.read()

simulatedAnnealingReader = resultadosFileReader("Resultados/resultadoTreinamentoSimulated Annealing.result")
resultadosTreinamentos["Simulated Annealing"] = simulatedAnnealingReader.read()

geneticoReader = resultadosFileReader("Resultados/resultadoTreinamentoAlgoritmo Genetico.result")
resultadosTreinamentos["Algoritmo Genetico"] = geneticoReader.read()

# Impressão dos BoxPlots
tempos = list()
nomes = list()

for nome, meta in resultadosTreinamentos.items():
    nomes.append(nome)
    tempos.append(pd.DataFrame(meta[2]).assign(Algoritmo = nome))
    meta = meta[3]
    resultados = list()
    i = 1
    with open("Resultados/ResultadosTreinamento"+nome+".legenda", "w") as legenda:
        for resposta in meta:
            aux = list()
            for resp in resposta["Resultados"]:
                aux.append(resp[1])
            resultados.append(pd.DataFrame(aux).assign(Hiperparametros = i))
            legenda.write(str(i) + ":" + str(resposta["Parametros"])+"\n")
            i += 1
    # Boxplot dos resultados de treinamento
    resultados = pd.concat(resultados)
    resultados = pd.melt(resultados, id_vars=["Hiperparametros"], value_name="Resultados")
    sea.boxplot(x = "Hiperparametros", y = "Resultados", data= resultados)
    plt.title("Resultados Treinamento "+nome)
    plt.savefig("Resultados/ResultadosTreinamento"+ nome +".png")
    

# Boxplot dos tempos de treinamento
tempos = pd.concat(tempos)
tempos = pd.melt(tempos, id_vars=["Algoritmo"],value_name="Tempo")
sea.boxplot(x = "Algoritmo", y = "Tempo", data = tempos)
plt.title("Tempos de Treinamento")
plt.savefig("Resultados/TemposTreinamento.png")

import scriptTeste

# Leitura dos arquivos de resultados
resultadosTestes = { }

hillClimbingReader = resultadosFileReader("Resultados/resultadoFinalHill Climbing.result")
resultadosTestes["Hill Climbing"] = hillClimbingReader.read()

graspReader = resultadosFileReader("Resultados/resultadoFinalGRASP.result")
resultadosTestes["GRASP"] = graspReader.read()

simulatedAnnealingReader = resultadosFileReader("Resultados/resultadoFinalSimulated Annealing.result")
resultadosTestes["Simulated Annealing"] = simulatedAnnealingReader.read()

beamSearchReader = resultadosFileReader("Resultados/resultadoFinalBeam Search.result")
resultadosTestes["Beam Search"] = beamSearchReader.read()

geneticoReader = resultadosFileReader("Resultados/resultadoFinalAlgoritmo Genetico.result")
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
with open("Resultados/MediasStd.txt", "w") as fp:
    fp.write("Algoritmo\tMedia Absoluta\tDesvio Absoluto\tMedia Normalizada\tDesvio Normalizado\tMedia Tempo\tDesvio Tempo\n")
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
        fp.write(str(al)+ "\t" + str(meanstdHeuristicas[al][0]) + "\t" + str(meanstdHeuristicas[al][1]) + "\t" + str(meanstdNormalizadas[al][0]) + "\t" + str(meanstdNormalizadas[al][1]) + "\t" + str(meanstdTempos[al][0]) + "\t" + str(meanstdTempos[al][1]) + "\n")

# Impressão dos BoxPlots
tempos = list()
nomes = list()
resultados = list()
for nome, meta in resultadosTestes.items():
    nomes.append(nome)
    tempos.append(pd.DataFrame(meta[1]).assign(Algoritmo = nome))
    meta = meta[0]
    aux = list()
    for resposta in meta:
        resposta = resposta["Resultados"]["Resposta"]
        aux.append(resposta[1])
    resultados.append(pd.DataFrame(aux).assign(Algoritmo = nome))

resultadosNorm = list()
for nome, meta in normalizadoPorHeuristica.items():
    resultadosNorm.append(pd.DataFrame(meta).assign(Algoritmo = nome))

# Boxplot dos tempos de treinamento
tempos = pd.concat(tempos)
tempos = pd.melt(tempos, id_vars=["Algoritmo"],value_name="Tempo")
sea.boxplot(x = "Algoritmo", y = "Tempo", data = tempos)
plt.title("Tempos de Teste")
plt.savefig("Resultados/TemposTeste.png")

# Boxplot dos resultados de treinamento
resultados = pd.concat(resultados)
resultados = pd.melt(resultados, id_vars=["Algoritmo"], value_name="Resultados")
sea.boxplot(x = "Algoritmo", y = "Resultados", data= resultados)
plt.title("Resultados de Teste")
plt.savefig("Resultados/ResultadosTeste.png")

resultadosNorm = pd.concat(resultadosNorm)
resultadosNorm = pd.melt(resultadosNorm, id_vars=["Algoritmo"], value_name="Resultados")
sea.boxplot(x = "Algoritmo", y = "Resultados", data= resultadosNorm)
plt.title("Resultados Normalizados de Teste")
plt.savefig("Resultados/ResultadosNormalizadosTeste.png")
