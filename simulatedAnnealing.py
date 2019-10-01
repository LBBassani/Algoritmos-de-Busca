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
import threading
from time import time
import random

def simulatedAnnealing(problema, estado, t, a, minT, numIter, tempo = 0):

    # Rotina de tempo limite
    def saida(encerrou):
        if tempo > 0:
            encerrou.clear()
            encerrou.append([True])

    encerrou = list()
    encerrou.append([False])
    inicio = time()
    print(inicio)

    t = threading.Timer(tempo*60, saida, encerrou)
    t.start()

    melhorEstado = estado.copy()
    aux = estado.copy()

    # while t > minT:
    while True:
        if encerrou[0][0]:
            print("encerrou")
            print(encerrou)
            break
        _ = problema.gerarVizinhos(aux, todaVizinhanca = True)

    estado.clear()
    estado.extend(melhorEstado)
    final = time()
    print(final)
    t.join()
    print("retornando")
    return final - inicio

"""        viz = problema.gerarVizinhos(aux, todaVizinhanca = True)
         for _ in range(1, numIter):
            if len(viz) == 0:
                break
            vizinho = viz.pop(random.randint(0, len(viz)-1))
            if problema.aceitarVizinho(aux, vizinho, t):
                aux = vizinho
                viz = problema.gerarVizinhos(aux, todaVizinhanca = True)
                if problema.melhorEstado([aux, melhorEstado]) == aux:
                    melhorEstado = aux
        t = t*a """