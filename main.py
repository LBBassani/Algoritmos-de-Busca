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
from hillClimbing import hillClimbing
from beamSearch import beamSearch
from simulatedAnnealing import simulatedAnnealing
from genetico import algoritmoGenetico
from grasp import grasp

""" Testes dos algoritmos """
def teste():
    paramHC = None
    paramBS = {"nEstados" : 3}
    paramSA = {"t" : 50, "a" : 0.6, "minT" : 1, "numIter" : 3}
    paramAG = {"maxIter" : 10, "tamanhoPop" : 3, "maxSemMelhora" : 15, "chanceCross" : 0.5, "chanceMutacao" : 0.5}
    paramGP = {"m" : 2, "numIter" : 50, "metodoBuscaLocal" : [simulatedAnnealing, paramSA]}
    try:
        m = mochila([(1, 3), (4, 6), (5, 7)], 19)
        metodos = [[hillClimbing, paramHC], [beamSearch, paramBS] , [simulatedAnnealing, paramSA], [algoritmoGenetico, paramAG], [grasp, paramGP]]
        estado = list()
        for metodo in metodos:
            if metodo[1]:
                m.busca(estado, metodo[0], **metodo[1])
            else:
                m.busca(estado,metodo[0])
            print("Resultado do Teste com", metodo[0].__name__, ":", estado, "Valor :", m.valorAtual(estado), "Tamanho :", m.tamanhoAtual(estado))
            estado = m.estadoNulo()
    except NotImplementedError:
        print("Algum método não está implementado")
    finally:
        print("Final do Teste :)")

teste()