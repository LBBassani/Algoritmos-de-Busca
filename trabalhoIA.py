""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
import IProblema
import threading
from genetico import algoritmoGenetico as genetico
from mochila import mochila


class treinamento:

    def __init__(self, problemas, metodo, **keyargs ):
        self.problema = problemas
        self.metodo = metodo
        self.parametros = keyargs
    
    
    def treino(self, tempo = 0):
        try:
            pass 
        except IProblema.TimedOutExc:
            raise
        

class teste:

    def __init__(self, problemas, metodo, **keyargs):
        self.problemas = problemas
        self.metodo = metodo
        self.parametros = keyargs

    def realizaTeste(self, estado, tempo = list()):
        try:
            pass 
        except IProblema.TimedOutExc:
            raise