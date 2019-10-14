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

parametrosTreinamento = {
    "Beam Search" : {"nEstados" : [10, 25, 50, 100]},
    "Simulated Annealing" : {"t" : [50, 90, 100, 250, 500], "a" : [0.7, 0.85, 0.9, 0.95, 0.97, 0.99], "minT" : [1], "numIter" : [50, 100, 200, 350, 500]},
    "Algoritmo Genético" : {"maxIter" :  [50, 100, 200, 350, 500], "tamanhoPop" : [10, 20, 30], "maxSemMelhora" : [15], "chanceCross" : [0.75, 0.85, 0.95], "chanceMutacao" : [0.1, 0.2, 0.3]},
    "GRASP" : {"m" : [2, 5, 10, 15], "numIter" : [50, 100, 200, 350, 500], "metodoBuscaLocal" : [[deepestDescent, None]]},
}

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

# algoritmos a serem treinados
treinamentos = {
    "Algoritmo Genético" : trabalhoIA.treinamento(problemasTreino, algoritmoGenetico, **parametrosTreinamento["Algoritmo Genético"]),
    "Simulated Annealing" : trabalhoIA.treinamento(problemasTreino, simulatedAnnealing, **parametrosTreinamento["Simulated Annealing"]),
    "Beam Search" : trabalhoIA.treinamento(problemasTreino, beamSearch, **parametrosTreinamento["Beam Search"]),
    "GRASP" : trabalhoIA.treinamento(problemasTreino, grasp, **parametrosTreinamento["GRASP"])
}

# resultados dos treinamentos
resultadosTreinamentos = {
    "Algoritmo Genético" : treinamentos["Algoritmo Genético"].realizaTreino(2),
    "Simulated Annealing" : treinamentos["Simulated Annealing"].realizaTreino(2),
    "Beam Search" : treinamentos["Beam Search"].realizaTreino(2),
    "GRASP" : treinamentos["GRASP"].realizaTreino(2)
}

print(resultadosTreinamentos["Algoritmo Genético"])
print(resultadosTreinamentos["Simulated Annealing"])
print(resultadosTreinamentos["Beam Search"])
print(resultadosTreinamentos["GRASP"])

# problemas de Teste de acordo com apendice A do enunciado do primeiro trabalho de IA
""" problemasTeste = {
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
} """

# resultados dos testes
""" resultadosTestes = {
    "Hill Climbing" : trabalhoIA.teste(problemasTeste, hillClimbing).realizaTeste(5),
    "Beam Search" : trabalhoIA.teste(problemasTeste, beamSearch).realizaTeste(5),
    "Simulated Annealing" : trabalhoIA.teste(problemasTeste, simulatedAnnealing).realizaTeste(5),
    "GRASP" : trabalhoIA.teste(problemasTeste, grasp).realizaTeste(5),
    "Algoritmo Genético" : trabalhoIA.teste(problemasTeste, algoritmoGenetico).realizaTeste(5)
} """