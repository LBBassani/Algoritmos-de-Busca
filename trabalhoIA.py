""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
import IProblema

""" Classe de Treinameto
        Atributos :
            problemas   : Dicionário de problemas a serem utilizados para o treinamento do método
            metodo      : Método a ser treinado
            parametros  : dicionário com listas de parâmetros a serem testados
            resposta    : objeto contendo as respostas do treinamento após realizado (None antes de treinar)

        Métodos :
            realizaTreino
                Descrição : Método de treinamento de algoritmos que, com base nos parametros passados 
                            na construção da classe, realiza uma busca em grade dos parametros com melhor
                            desempenho nos casos de treinamento.
                Parametros : Sim
                    tempo    : tempo limite de execução de cada tentativa de rodar um problema
                Retorno    : Não
                Lança exceções : Sim
                    IProblema.TimedOutExec  : Exceção de tempo limite
                    NotImplementedError     : Erro de método não implementado por subclasse de IProblema
"""
class treinamento:

    def __init__(self, problemas, metodo, **keyargs ):
        self.problemas = problemas
        self.metodo = metodo
        self.parametros = keyargs
        self.resposta = None
    
    
    def realizaTreino(self, tempo = list()):
        try:
            pass 
        except IProblema.TimedOutExc:
            raise


""" Classe de Teste
        Atributos :
            problemas   : Dicionário de problemas a serem utilizados para o teste do método
            metodo      : Método a ser testado
            parametros  : dicionário com listas de parâmetros a serem testados
            resposta    : objeto contendo as respostas do teste após realizado (None antes de testar)

        Métodos :
            realizaTreino
                Descrição : Método de teste de algoritmos que, com base nos parametros passados 
                            na construção da classe, avalia o desempenho do método nos casos de teste.
                Parametros : Sim
                    tempo    : tempo limite de execução de cada tentativa de rodar um problema
                Retorno    : Não
                Lança exceções : Sim
                    IProblema.TimedOutExec  : Exceção de tempo limite
                    NotImplementedError     : Erro de método não implementado por subclasse de IProblema
"""
class teste:

    def __init__(self, problemas, metodo, **keyargs):
        self.problemas = problemas
        self.metodo = metodo
        self.parametros = keyargs
        self.resposta = None

    def realizaTeste(self, estado, tempo = list()):
        try:
            pass 
        except IProblema.TimedOutExc:
            raise