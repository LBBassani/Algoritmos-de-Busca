from ioTools import ParamFileReader, resultadosFileWriter
from Busca.ProblemasBusca.mochila import mochila
from Busca.AlgoritmosBusca.beamSearch import beamSearch
from Busca.AlgoritmosBusca.simulatedAnnealing import simulatedAnnealing
from Busca.AlgoritmosBusca.genetico import algoritmoGenetico
from Busca.AlgoritmosBusca.grasp import grasp
import trabalhoIA

# Problemas de Treino de acordo com apendice A do enunciado do primeiro trabalho de IA
problemasTreino = {
    "m1"  : mochila([(1, 3), (4, 6), (5, 7)], 19),
    "m3"  : mochila([(1, 3), (4, 6), (5, 7), (3, 4)], 58),
    "m4"  : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (8, 10), (4, 8), (3, 5), (6, 9)], 58),
    "m6"  : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (8, 10), (4, 8), (3, 5), (6, 9), (2, 1)], 58),
    "m8"  : mochila([(1, 2), (2, 3), (4, 5), (5, 10), (14, 15), (15, 20), (24, 25), (29, 30), (50, 50)], 120),
    "m9"  : mochila([(1, 2), (2, 3), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 30), (50, 50)], 120),
    "m11" : mochila([(24, 25), (29, 30), (50, 50)], 120),
    "m14" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8), (1, 2), (2, 3), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 30), (50, 50)], 138),
    "m17" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8), (1, 2), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 37)], 13890000),
    "m20" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (1, 2), (3, 5), (7, 10), (10, 15), (13, 20), (15, 20)], 45678901)
}

# Leitura dos Parametros
paramFileReader = ParamFileReader("parametros.param")
parametros = paramFileReader.read()

# algoritmos a serem treinados
treinamentos = {
    # "Algoritmo Genetico" : trabalhoIA.treinamento(problemasTreino, algoritmoGenetico, **parametros["Algoritmo Genetico"]),
    # "GRASP" : trabalhoIA.treinamento(problemasTreino, grasp, **parametros["GRASP"]),
    "Simulated Annealing" : trabalhoIA.treinamento(problemasTreino, simulatedAnnealing, **parametros["Simulated Annealing"]),
    # "Beam Search" : trabalhoIA.treinamento(problemasTreino, beamSearch, **parametros["Beam Search"])
}

# resultados dos treinamentos
resultadosTreinamentos = { }
for key, value in treinamentos.items():
    resultadosTreinamentos[key] = value.realizaTreino()
    nomeArq = "resultadoTreinamento" + key + ".result"
    resulwriter = resultadosFileWriter(nomeArq)
    resulwriter.write(resultadosTreinamentos[key])
