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

def simulatedAnnealing(problema, estado, t, a, minT, numIter, tempo = list()):

    # Rotina de tempo limite
    encerrou = list()
    encerrou.append([False])

    if tempo:
        
        def saida(encerrou):
        
                encerrou.clear()
                encerrou.extend([True])

        t = threading.Timer(tempo[0]*60, saida, encerrou)
        t.start()
    
    inicio = time()
    melhorEstado = estado.copy()
    aux = estado.copy()

    try:
        # while t > minT:
        while True:
            if encerrou[0][0]:
                raise IProblema.TimedOutExc
            _ = problema.gerarVizinhos(aux, todaVizinhanca = True)
    except IProblema.TimedOutExc:
        print("Terminou por Timeout")
        raise
    else:
        if tempo:
            t.cancel()
    finally:
        estado.clear()
        estado.extend(melhorEstado)
        final = time()
        if tempo: 
            t.join()
            tempo.clear()        
        tempo.append(final - inicio)

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