""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
import IProblema
import threading
from simulatedAnnealing import simulatedAnnealing
from mochila import mochila


class treinamento:

    def __init__(self, problemas, metodo, **keyargs ):
        self.problema = problemas
        self.metodo = metodo
        self.parametros = keyargs
    
    
    def treino(self, tempo = 0):
        pass
        

class teste:

    def __init__(self, problemas, metodo, **keyargs):
        self.problemas = problemas
        self.metodo = metodo
        self.parametros = keyargs

    def realizaTeste(self, estado, tempo = list()):
        try:
            self.metodo(self.problemas[0], estado, **self.parametros, tempo = tempo) 
        except IProblema.TimedOutExc:
            raise

m = mochila([(1, 3), (4, 6), (5, 7)], 19)
parametros = {"t" : 50, "a" : 0.7, "minT" : 1, "numIter" : 50}
t = teste([m], simulatedAnnealing, **parametros)
estado = m.estadoAleatorio()
tempo = [0.2]
try:
    t.realizaTeste(estado, tempo = tempo)
except IProblema.TimedOutExc:
    print("Terminou por Timeout")
finally:
    print("Estado:", estado)
    print("Tempo:", tempo[0])