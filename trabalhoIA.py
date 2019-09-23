""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
import IProblema


class treinamento:

    def __init__(self, problema, metodo, **keyargs ):
        self.problema = problema
        self.metodo = metodo
        self.parametros = keyargs
    
    def treino(self):
        pass

class teste:

    def __init__(self, problema, metodos):
        self.problema = problema
        self.metodos = metodos

    def realizaTeste(self):
        pass