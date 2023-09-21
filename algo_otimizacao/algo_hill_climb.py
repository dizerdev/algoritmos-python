import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from representacao import pessoas, destino, voos, imprimir_voos


def fitness_function(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
    return total_preco


fitness = mlrose.CustomFitness(fitness_function)
problema = mlrose.DiscreteOpt(length=12,
                              fitness_fn=fitness,
                              maximize=False,
                              max_val=10)

melhor_solucao, melhor_custo = mlrose.hill_climb(problema, random_state=1)
melhor_solucao, melhor_custo

imprimir_voos(melhor_solucao)
