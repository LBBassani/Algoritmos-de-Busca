""" Metodo GRASP (Greedy Randomized Adaptive Search)
        Classe : Baseada em Soluções Completas -> Busca Local
        Hiperparametros : 
            m : elementos para escolher no construtor guloso de estados
            numIter : número de iterações total do algoritmo (critério de parada)
        Necessita de Estado Inicial : Não
"""
import IProblema
import random
import threading
from time import time

def grasp(problema, estado, m, numIter, metodoBuscaLocal, tempo = list()):

    # Rotina de tempo limite
    encerrou = list()
    encerrou.append([False])

    if tempo:
        
        def saida(encerrou):
                encerrou.clear()
                encerrou.extend([True])

        temporizador = threading.Timer(tempo[0]*60, saida, encerrou)
        temporizador.start()
    
    inicio = time()

    melhor = problema.estadoNulo()
    try:
        for _ in range(0, numIter):
            if encerrou[0][0]:
                raise IProblema.TimedOutExc
            novoEstado = problema.estadoNulo()
            problema.construcaoGulosa(novoEstado, m, random.randint(0, 100))
            problema.buscaLocal(novoEstado, metodoBuscaLocal[0], **metodoBuscaLocal[1])
            if problema.melhorEstado([melhor, novoEstado]):
                melhor = novoEstado
        
    except IProblema.TimedOutExc:
        raise
    else:
        if tempo:
            temporizador.cancel()
    finally:
        estado.clear()
        estado.extend(melhor)
        final = time()
        if tempo: 
            temporizador.join()
            tempo.clear()        
        tempo.append(final - inicio)
