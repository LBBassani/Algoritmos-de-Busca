""" Metodo Tabu Search
        Classe : Baseada em Soluções Completas -> Busca Local
        Hiperparametros : 
                numIter : numéro de iterações do algoritmo (critério de parada)
        Necessita de Estado Inicial : Sim
"""

from ..ProblemasBusca import IProblema

def tabuSearch(problema, estado, numIter):
    melhor = list()
    melhor.extend(estado)
    listaTabu = list()
    for _ in range(0, numIter):
        expansao = problema.gerarVizinhos(estado, todaVizinhanca = True)
        while expansao:
            viz = problema.melhorEstado(expansao)
            if listaTabu.count(viz) == 0:
                break
            expansao.remove(viz)
        if not viz:
            break
        if problema.melhorEstado([viz, melhor]) == viz:
            melhor.clear()
            melhor.extend(viz)
        if listaTabu.count(viz) == 0:
            estado.clear()
            estado.extend(viz)
            listaTabu.append(viz)
    estado.clear()
    estado.extend(melhor)
    print(melhor)