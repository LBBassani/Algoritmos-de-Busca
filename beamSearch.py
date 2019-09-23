""" Metodo Beam Search
        Classe : Baseada em Soluções Parciais
        Hiperparametros : 
            nEstados : número de estados mantidos na expansão
        Necessita de Estado Inicial : Não
"""
import IProblema

def beamSearch(problema, estado, nEstados):
    estados = [problema.estadoNulo()]
    estados.extend(problema.gerarVizinhos(estados[0]))
    estados = problema.escolheMelhores(estados, nEstados)
    melhor = []

    while len(estados) > 0:
        melhor = estados[0]
        avaliar = estados.copy()
        for e in avaliar:
            estados.remove(e)
            estados.extend(problema.gerarVizinhos(e))
        estados = problema.escolheMelhores(estados, nEstados)
    estado.clear()
    estado.extend(melhor)
