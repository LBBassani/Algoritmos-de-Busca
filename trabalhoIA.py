""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
import IProblema
import threading
from simulatedAnnealing import simulatedAnnealing
from mochila import mochila

class TimedOutExc(Exception):
    pass


class treinamento:

    def __init__(self, problemas, metodo, **keyargs ):
        self.problema = problemas
        self.metodo = metodo
        self.parametros = keyargs
    
    
    def treino(self, tempo = 0):
        def exiting(retorno):
            retorno.clear()
            retorno.append([True])

        retorno = list()
        retorno.append([False])
        t = threading.Timer(tempo*60, exiting, retorno)
        t.start()
        while True:
            if retorno[0]:
                break
        print("Terminou")
        

class teste:

    def __init__(self, problemas, metodo, **keyargs):
        self.problemas = problemas
        self.metodo = metodo
        self.parametros = keyargs

    def realizaTeste(self, estado, tempo = 0):
        return self.metodo(self.problemas[0], estado, **self.parametros, tempo = tempo)

m = mochila([(1, 3), (4, 6), (5, 7)], 19)
parametros = {"t" : 50, "a" : 0.7, "minT" : 1, "numIter" : 50}
t = teste([m], simulatedAnnealing, **parametros)
estado = m.estadoAleatorio()
resposta = t.realizaTeste(estado, tempo = 0.1)
print("Estado: ", estado)
print("Tempo")
print(resposta)