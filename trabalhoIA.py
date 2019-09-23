""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
import IProblema


class treinamento:

    def __init__(self, problemas, metodo, **keyargs ):
        self.problema = problemas
        self.metodo = metodo
        self.parametros = keyargs
    
    def treino(self, tempo = 0):
        pass

class teste:

    def __init__(self, problemas, metodo):
        self.problemas = problemas
        self.metodo = metodo

    def realizaTeste(self, tempo = 0):
        pass