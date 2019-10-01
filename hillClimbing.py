""" Metodo Hill Climbing
        Classe : Baseada em Soluções Parciais
        Hiperparametros : Não tem
        Necessita de Estado Inicial : Não
"""
import IProblema
from time import time
import threading

def hillClimbing(problema, estado, tempo = list()):
    
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
    aux = problema.melhorEstado(problema.gerarVizinhos(melhor))

    try:
        while len(aux) != 0 :
            if encerrou[0][0]:
                raise IProblema.TimedOutExc
            melhor = aux
            aux = problema.melhorEstado(problema.gerarVizinhos(melhor))

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