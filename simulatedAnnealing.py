""" Metodo Simulated Annealing
        Classe : Baseada em Soluções Completas -> Busca Local
        Hiperparametros :
            t : temperatura inicial
            a : taxa de queda de temperatura
            minT : temperatura mínima (critério de parada)
            numIter : quantidade de iterações por temperatura
        Necessita de Estado Inicial : Sim
"""
import IProblema
import random

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
