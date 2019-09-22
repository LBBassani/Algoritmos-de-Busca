# Algoritmos de Busca
Este trabalho é dedicado a algoritmos de busca estudados em Inteligência Artificial. Alguns algoritmos foram implementados com finalidade de estudos para a primeira prova e alguns para o primeiro trabalho prático da matéria de Inteligência Artificial no semestre de 2019/02, pela Aluna Lorena Bassani do curso de Ciência da Computação da Universidade Federal do Espírito Santo - UFES.

## Primeiro Trabalho de IA
O primeiro trabalho prático de Inteligência Artificial se dedica a encontrar hiperparâmetros e testar cinco métodos de busca aplicados ao problema da mochila. Abaixo estão listados os métodos implementados para o trabalho:

### Hill Climbing
**Classe** : Baseada em Soluções Parciais<br>
**Descrição** : Procedimento de Estratégia Gulosa que procura construir a solução escolhendo sempre o melhor próximo estado, sem *backtracking*.<br>
**Necessita de Estado Inicial** : Não<br>
**Hiperparametros** : Não tem

### Beam Search
**Classe** : Baseada em Soluções Parciais<br>
**Descrição** : Algoritmo de Busca em amplitude, onde ao invés de utilizar apenas o melhor próximo estado, estuda as possibilidades de vários próximos estados expandindo-os. O número de estados estudados é passado como parâmetro.<br>
**Necessita de Estado Inicial** : Não<br>
**Hiperparametros** : 
* nEstados : número de estados mantidos na expansão

### Simulated Annealing
**Classe** : Baseada em Soluções Completas -> Busca Local <br>
**Descrição** : Baseado em processo físico de resfriamento de sólido superaquecido, onde durante o resfriamento podem ocorrer algumas etapas de medição de aquecimento, representado no algoritmo por uma chance de aceitar um estado pior que o atual. Quanto menor a "temperatura" menos o fenomeno de reaquecimento ocorre, ou seja, menor a chance de aceitarmos estados piores.<br>
**Necessita de Estado Inicial** : Sim<br>
**Hiperparametros** :
* t : temperatura inicial
* a : taxa de queda de temperatura
* minT : temperatura mínima (critério de parada)
* numIter : quantidade de iterações por temperatura

### GRASP - Greedy Randomized Adaptive Search
**Classe** : Baseada em Soluções Completas -> Busca Local<br>
**Descrição** : É um método iterativo probabilístico, onde cada iteração obtém uma solução independente do problema em estudo e é composta de duas fases:
1. *Fase Construtiva* : Determina uma solução a partir de uma função gulosa probabilística
2. *Fase de Busca Local* : Submeter a solução a um outro algoritmo de busca local.

**Necessita de Estado Inicial** : Não<br>
**Hiperparametros** : 
* m : elementos para escolher no construtor guloso de estados
numIter : número de iterações total do algoritmo (critério de parada)

### Algoritmo Genético
**Classe** : Baseada em Soluções Completas -> Busca Populacional -> Computação Evolutiva<br>
**Descrição** : Algoritmo evolutivo baseado na teoria de seleção natural e hereditariedade, que trabalha em cima do conceito de gerações de uma população. Cada geração é composta por descendentes da geração anterior (recombinações ou mutações desses individuos) e são selecionados para continuar os melhores descendentes, com chances de alguns descendentes piores serem escolhidos no lugar de alguns melhores por fator aleatório.<br>
**Necessita de Estado Inicial** : Não<br>
**Hiperparametros** : 
* maxIter : número máximo de iterações (critério de parada)
* tamanhoPop : tamanho da população
* maxSemMelhora : número máximo de iterações sem melhora de resposta (critério de parada)
* chanceCross : chance de ocorrer crossover
* chanceMutacao : chance de ocorrer mutação
