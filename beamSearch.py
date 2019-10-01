""" Metodo Beam Search
        Classe : Baseada em Soluções Parciais
        Hiperparametros : 
            nEstados : número de estados mantidos na expansão
        Necessita de Estado Inicial : Não
"""
import IProblema
from time import time
import threading

def beamSearch(problema, estado, nEstados, tempo = list()):

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

    estados = [problema.estadoNulo()]
    estados.extend(problema.gerarVizinhos(estados[0]))
    estados = problema.escolheMelhores(estados, nEstados)
    melhor = []
    try:
        while len(estados) > 0:
            if encerrou[0][0]:
                raise IProblema.TimedOutExc
            melhor = estados[0]
            avaliar = estados.copy()
            for e in avaliar:
                estados.remove(e)
                estados.extend(problema.gerarVizinhos(e))
            estados = problema.escolheMelhores(estados, nEstados)

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