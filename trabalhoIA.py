""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
import IProblema
from sklearn.model_selection import ParameterGrid


""" Classe de Treinameto
        Atributos :
            problemas   : Dicionário de problemas a serem utilizados para o treinamento do método
            metodo      : Método a ser treinado
            parametros  : dicionário com listas de parâmetros a serem testados
            respostaProblema : objeto contendo as respostas por problema do treinamento após realizado (não existe antes de treinar)
            respostaParametros : objeto contendo as respostas por parametro do treinamento após realizado (não existe antes de normalizar os resultados)
            respostaProblemaNormal : objeto contendo as respostas normalizadas por problema do treinamento após realizado (não existe antes de normalizar os resultados)

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
        self.parametros = ParameterGrid(keyargs)
    
    
    def realizaTreino(self, tempo = [2]):
        """ primeiro passo : criar grade de parametros 
                Como : Usando ParameterGrid do Scikit-learn
        """
        
        if tempo:
            timeout = tempo[0]
        else:
            timeout = 2 # Tempo de timeout default de 2 minutos
        
        """ segundo passo : Rodar os testes 
                Como :  Para cada problema a ser usado para treino roda o algoritmo
                            para cada combinação de parametros vindos da grid de parametros.
                        Guarda o resultado de tempo, resposta e lista de parametros
        """
        for nome, p in self.problemas.items():
            self.respostaProblema = list()
            resultados = list()
            for paramList in self.parametros:
                # prepara as variáveis para o problema
                terminou = True
                estado = p.estadoNulo()
                tempo.clear()
                tempo.append(timeout)
                # Realiza a busca
                try:
                    p.busca(estado, self.metodo, tempo, **paramList)
                except IProblema.TimedOutExc:
                    # Se veio com timeout, muda a flag de termino para False
                    terminou = False
                # Formata a resposta
                resp = {"Tempo" : tempo[0], "Resposta" : [estado.copy(), p.aptidao(estado)], "Parametros" : paramList, "Terminou" : terminou}
                resultados.append(resp)
            resp = {"Problema" : (nome, p.descricao()), "Resultados" : resultados}
            self.respostaProblema.append(resp)  

    def resultadosPorParametros(self):
        """ Montar os resultados por parametros """
        self.respostaParametros = list()
        pass

    def resultadosNormalizados(self):
        """ Normalizar os resultados por problema do conjunto de treino """
        self.respostaProblemaNormal = self.respostaProblema.copy()
        mini, maxi = self.minMaxValueResultadosPorProblema()
        divisor = maxi - mini
        for r in self.respostaProblemaNormal:
            resultados = r["Resultados"]
            for resultado in resultados:
                resp = resultado["Resposta"]
                resp[1] = (resp[1] - mini)/divisor


    def mediaResultadosPorProblema(self):
        aux = self.aptidoesResultados()
        media = sum(aux)
        media = media/(len(self.respostaProblema)*len(self.problemas))
        return media
    
    def minMaxValueResultadosPorProblema(self):
        aux = self.aptidoesResultados()
        return (min(aux), max(aux))

    def aptidoesResultados(self):
        aux = list(map(lambda x: x["Resultados"], self.respostaProblema))
        aux = [item for sublist in aux for item in sublist]
        aux = list(map(lambda x : x["Resposta"], aux))
        aux = list(map(lambda x: x[1], aux))
        return aux

    def melhoresParametros(self):
        """ Encontrar o melhor resultado """
        pass

    def temposAlcancados(self):
        """ Retornar os tempos """
        tempos = list()
        for resp in self.respostaProblema:
            resultado = resp["Resultados"]
            for r in resultado:
                tempo = r["Tempo"]
                tempos.append(tempo)
        return tempos

""" Classe de Teste
        Atributos :
            problemas   : Dicionário de problemas a serem utilizados para o teste do método
            metodo      : Método a ser testado
            parametros  : dicionário com listas de parâmetros a serem testados
            resposta    : objeto contendo as respostas do teste após realizado (none antes de testar)

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