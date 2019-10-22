import IProblema
import random as r
import math as m
import threading
from time import time

def deepestDescent(problema, estado, tempo = None):
    encerrou = list()
    encerrou.append([False])

    if tempo:      
        def saida(encerrou):
                encerrou.clear()
                encerrou.extend([True])

        temporizador = threading.Timer(tempo[0]*60, saida, encerrou)
        temporizador.start()
    
    inicio = time()

    viz = list(list())
    melhorEstado = estado.copy()

    try:
        while len(viz) != 0:
            if encerrou[0][0]:
                raise IProblema.TimedOutExc
            viz = problema.gerarVizinhos(melhorEstado, todaVizinhanca = True)
            viz = problema.escolheMelhoresDescent(melhorEstado, viz)
            melhorViz = problema.melhorEstado(viz)
            if len(melhorViz) != 0:
                melhorEstado = melhorViz
    except IProblema.TimedOutExc:
        raise
    else:
        if tempo:
            temporizador.cancel()
    finally:
        estado.clear()
        estado.extend(melhorEstado)
        final = time()
        if tempo: 
            temporizador.join()
            tempo.clear()        
        tempo.append(final - inicio)

def multistartDescent(problema, estado, maxIter, tempo = None):
    i = 0
    melhorEstado = problema.estadoNulo()

    while i < maxIter:
        resultado = problema.estadoAleatorio()
        deepestDescent(problema, resultado)
        if problema.melhorEstado([resultado, melhorEstado]) == resultado:
            melhorEstado = resultado
        i = i + 1
    
    estado.clear()
    estado.extend(melhorEstado)
