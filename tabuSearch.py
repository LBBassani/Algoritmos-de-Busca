""" Metodo Tabu Search
        Classe : Baseada em Soluções Completas -> Busca Local
        Hiperparametros : (Desconhecido)
        Necessita de Estado Inicial : (Desconhecido)
"""

import IProblema

def tabuSearch(problema, estado):
    melhorEstado = problema.estadoAleatorio()
    # TODO : Implementar Tabu Search
    estado.clear()
    estado.extend(melhorEstado)