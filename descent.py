import Iproblema
import random as r
import math as m

def deepestDescent(problema, estado):
    viz = list(list())
    melhorEstado = estado.copy()

    while len(viz) != 0:
        viz = problema.gerarVizinhos(melhorEstado, todaVizinhanca = True)
        viz = problema.escolheMelhores(melhorEstado, viz)
        melhorViz = problema.melhorEstado(viz)
        if len(melhorViz) != 0:
            melhorEstado = melhorViz
    
    estado.clear()
    estado.extend(melhorEstado)

def multistartDescent(problema, estado, maxIter):
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
