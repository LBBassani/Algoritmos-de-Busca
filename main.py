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
from mochila import mochila
from hillClimbing import hillClimbing
from beamSearch import beamSearch
from simulatedAnnealing import simulatedAnnealing
from genetico import algoritmoGenetico
from grasp import grasp
from descent import deepestDescent
import trabalhoIA
import json

class ParamFileReader(object):
    def __init__(self, file):
        self.__f = file
    
    def read(self):
        with open(self.__f, "r") as f:
            params = {}
            line = f.readline()
            while line:
                if line.find("beginParam") >= 0:
                    metodo = f.readline().rstrip()
                    params[metodo] = {}
                    line = f.readline()
                    while line.find("endParam") < 0:
                        words = line.split()
                        param = words.pop(0)
                        params[metodo][param] = list()
                        tipo = words.pop(0)
                        tipo = list if tipo == "list" else int if tipo == "int" else float
                        for w in words:
                            params[metodo][param].append(tipo(w))
                        line = f.readline()
                line = f.readline()
            return params

class resultadosFileWriter(object):
    def __init__(self, file):
        self.__f = file

    def write(self, resultados):
        with open(self.__f, "w+") as f:
            f.write(json.dumps(resultados))

class resultadosFileReader(object):
    def __init__(self, file):
        self.__f = file
    
    def read(self):
        with open(self.__f, "r") as f:
            return json.load(f)

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

paramFileReader = ParamFileReader("parametros.param")
parametros = paramFileReader.read()

# algoritmos a serem treinados
treinamentos = {
    # "Algoritmo Genetico" : trabalhoIA.treinamento(problemasTreino, algoritmoGenetico, **parametros["Algoritmo Genetico"]),
    # "GRASP" : trabalhoIA.treinamento(problemasTreino, grasp, **parametros["GRASP"]),
    # "Simulated Annealing" : trabalhoIA.treinamento(problemasTreino, simulatedAnnealing, **parametros["Simulated Annealing"]),
    # "Beam Search" : trabalhoIA.treinamento(problemasTreino, beamSearch, **parametros["Beam Search"])
}

# resultados dos treinamentos
resultadosTreinamentos = { }
for key, value in treinamentos.items():
    resultadosTreinamentos[key] = value.realizaTreino()
    nomeArq = "resultadoTreinamento" + key + ".result"
    resulwriter = resultadosFileWriter(nomeArq)
    resulwriter.write(resultadosTreinamentos[key])

graspReader = resultadosFileReader("resultadoTreinamentoGRASP.result")
resultadosTreinamentos["GRASP"] = graspReader.read()

simulatedAnnealingReader = resultadosFileReader("resultadoTreinamentoSimulated Annealing.result")
resultadosTreinamentos["Simulated Annealing"] = simulatedAnnealingReader.read()

beamSearchReader = resultadosFileReader("resultadoTreinamentoBeam Search.result")
resultadosTreinamentos["Beam Search"] = beamSearchReader.read()

geneticoReader = resultadosFileReader("resultadoTreinamentoAlgoritmo Genetico.result")
resultadosTreinamentos["Algoritmo Genetico"] = geneticoReader.read()

print("Parametros Algoritmo Genetico:", resultadosTreinamentos["Algoritmo Genetico"][0][1])
print("Parametros Beam Search:", resultadosTreinamentos["Beam Search"][0][1])
print("Parametros Simulated Annealing:", resultadosTreinamentos["Simulated Annealing"][0][1])
print("Parametros GRASP:", resultadosTreinamentos["GRASP"][0][1])

# problemas de Teste de acordo com apendice A do enunciado do primeiro trabalho de IA
problemasTeste = {
    "m2"  : mochila([(1, 3), (4, 6), (5, 7)], 192), 
    "m5"  : mochila([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)], 287), 
    "m7"  : mochila([(1, 2), (2, 3), (4, 5), (5, 10), (14, 15), (13, 20), (24, 25), (29, 30), (50, 50)], 120), 
    "m10" : mochila([(1, 2), (2, 3), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 30), (50, 50)], 1240), 
    "m12" : mochila([(25, 26), (29, 30), (49, 50)], 104), 
    "m13" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8)], 138), 
    "m15" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8), (1, 2), (2, 3), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 30), (50, 50)], 13890), 
    "m16" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8), (1, 2), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 37)], 13890), 
    "m18" : mochila([(1, 3), (4, 6), (5, 7)], 190000), 
    "m19" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (1, 2), (3, 5), (7, 10), (10, 15), (13, 20), (15, 20)], 4567) 
}

# resultados dos testes
resultadosTestes = {
    "Hill Climbing" : trabalhoIA.teste(problemasTeste, hillClimbing),
    "Beam Search" : trabalhoIA.teste(problemasTeste, beamSearch, **resultadosTreinamentos["Beam Search"][0][1]),
    "Simulated Annealing" : trabalhoIA.teste(problemasTeste, simulatedAnnealing, **resultadosTreinamentos["Simulated Annealing"][0][1]),
    "GRASP" : trabalhoIA.teste(problemasTeste, grasp, **resultadosTreinamentos["GRASP"][0][1]),
    "Algoritmo Genético" : trabalhoIA.teste(problemasTeste, algoritmoGenetico, **resultadosTreinamentos["Algoritmo Genetico"][0][1])
}

for key, value in resultadosTestes.items():
    resultado = value.realizaTeste()
    nomeArq = "resultadoFinal" + key + ".result"
    writer = resultadosFileWriter(nomeArq)
    writer.write(resultado)