""" Metodo Hill Climbing
        Classe : Baseada em Soluções Parciais
        Hiperparametros : Não tem
        Necessita de Estado Inicial : Não
"""
import IProblema

def hillClimbing(problema, estado):
    melhor = problema.estadoNulo()
    aux = problema.melhorEstado(problema.gerarVizinhos(melhor))

    while len(aux) != 0 :
        melhor = aux
        aux = problema.melhorEstado(problema.gerarVizinhos(melhor))

    estado.clear()
    estado.extend(melhor)