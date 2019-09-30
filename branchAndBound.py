""" Metodo Branch and Bound
        Classe : Baseada em Soluções Parciais
        Hiperparametros :
            otimista : Define se a função heurística é otimista ou não
        Necessita de Estado Inicial : Sim
"""

import IProblema
from queue import PriorityQueue

def branch_and_bound(problema, estado, otimista):
    melhor = estado.copy()
    estadoInicial = problema.estadoNulo()
    fila = PriorityQueue()
    fila.put((problema.aptidao(estadoInicial), estadoInicial))
    while not fila.empty():
        estadoRetirado = fila.get()
        expandido = problema.gerarVizinhos(estadoRetirado[1])
        print(expandido)
        for i in expandido:
            if problema.valido(i):
                estimado = problema.estimativa(i, otimista)
                print(i, estimado)
                if problema.melhorEstado([estimado, melhor], validoOnly = False) == estimado:
                    if problema.melhorEstado([i, melhor]) == i:
                        melhor = i
                    fila.put((problema.aptidao(i), i))
    estado.clear()
    estado.extend(melhor)
