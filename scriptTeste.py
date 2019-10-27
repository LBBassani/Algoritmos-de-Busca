from ioTools import resultadosFileReader, resultadosFileWriter
from Busca.ProblemasBusca.mochila import mochila
from Busca.AlgoritmosBusca.hillClimbing import hillClimbing
from Busca.AlgoritmosBusca.beamSearch import beamSearch
from Busca.AlgoritmosBusca.simulatedAnnealing import simulatedAnnealing
from Busca.AlgoritmosBusca.genetico import algoritmoGenetico
from Busca.AlgoritmosBusca.grasp import grasp
import trabalhoIA

# Leitura dos Resultados do Treinamento
resultadosTreinamentos = { }

graspReader = resultadosFileReader("resultadoTreinamentoGRASP.result")
resultadosTreinamentos["GRASP"] = graspReader.read()

simulatedAnnealingReader = resultadosFileReader("resultadoTreinamentoSimulated Annealing.result")
resultadosTreinamentos["Simulated Annealing"] = simulatedAnnealingReader.read()

beamSearchReader = resultadosFileReader("resultadoTreinamentoBeam Search.result")
resultadosTreinamentos["Beam Search"] = beamSearchReader.read()

geneticoReader = resultadosFileReader("resultadoTreinamentoAlgoritmo Genetico.result")
resultadosTreinamentos["Algoritmo Genetico"] = geneticoReader.read()

# Apresenta os parametros decididos
print("Parametros Algoritmo Genetico:", resultadosTreinamentos["Algoritmo Genetico"][0][1])
print("Parametros Beam Search:", resultadosTreinamentos["Beam Search"][0][1])
print("Parametros Simulated Annealing:", resultadosTreinamentos["Simulated Annealing"][0][1])
print("Parametros GRASP:", resultadosTreinamentos["GRASP"][0][1])

# problemas de Teste de acordo com apendice A do enunciado do primeiro trabalho de IA
problemasTeste = {
    "m2"  : mochila([(1, 3), (4, 6), (5, 7)], 192), 
    "m5"  : mochila([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)], 287), 
    "m7"  : mochila([(1, 2), (2, 3), (4, 5), (5, 10), (14, 15), (13, 20), (24, 25), (29, 30), (50, 50)], 120), 
    "m10" : mochila([(1, 2), (2, 3), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 30), (50, 50)], 1240), 
    "m12" : mochila([(25, 26), (29, 30), (49, 50)], 104), 
    "m13" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8)], 138), 
    "m15" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8), (1, 2), (2, 3), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 30), (50, 50)], 13890), 
    "m16" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (2, 3), (6, 8), (1, 2), (3, 5), (7, 10), (10, 15), (13, 20), (24, 25), (29, 37)], 13890), 
    "m18" : mochila([(1, 3), (4, 6), (5, 7)], 190000), 
    "m19" : mochila([(1, 3), (4, 6), (5, 7), (3, 4), (2, 6), (1, 2), (3, 5), (7, 10), (10, 15), (13, 20), (15, 20)], 4567) 
}

# resultados dos testes
resultadosTestes = {
    # "Hill Climbing" : trabalhoIA.teste(problemasTeste, hillClimbing),
    # "Beam Search" : trabalhoIA.teste(problemasTeste, beamSearch, **resultadosTreinamentos["Beam Search"][0][1]),
    # "Simulated Annealing" : trabalhoIA.teste(problemasTeste, simulatedAnnealing, **resultadosTreinamentos["Simulated Annealing"][0][1]),
    # "GRASP" : trabalhoIA.teste(problemasTeste, grasp, **resultadosTreinamentos["GRASP"][0][1]),
    # "Algoritmo Genetico" : trabalhoIA.teste(problemasTeste, algoritmoGenetico, **resultadosTreinamentos["Algoritmo Genetico"][0][1])
}

# Realização dos Testes e escrita nos arquivos
for key, value in resultadosTestes.items():
    resultado = value.realizaTeste()
    nomeArq = "resultadoFinal" + key + ".result"
    writer = resultadosFileWriter(nomeArq)
    writer.write(resultado)
