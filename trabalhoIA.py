""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
import IProblema
import threading

class TimedOutExc(Exception):
    pass


class treinamento:

    def __init__(self, problemas, metodo, **keyargs ):
        self.problema = problemas
        self.metodo = metodo
        self.parametros = keyargs
    
    
    def treino(self, tempo = 0):
        melhores = self.parametros[0]
        def exiting():
            return melhores

        t = threading.Timer(tempo*60, exiting)
        t.start()
        while True:
            pass
        

class teste:

    def __init__(self, problemas, metodo):
        self.problemas = problemas
        self.metodo = metodo

    def realizaTeste(self, tempo = 0):
        pass