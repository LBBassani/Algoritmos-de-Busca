""" Metodo GRASP (Greedy Randomized Adaptive Search)
        Classe : Baseada em Soluções Completas -> Busca Local
        Hiperparametros : 
            m : elementos para escolher no construtor guloso de estados
            numIter : número de iterações total do algoritmo (critério de parada)
        Necessita de Estado Inicial : Não
"""
import IProblema
import random

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
