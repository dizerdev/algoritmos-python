import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


produtos = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]

espaco_disponivel = 3


def imprimir_solucao(solucao):
    for i in range(len(solucao)):
        if solucao[i] == 1:
            print('%s - %s' % (produtos[i][0], produtos[i][2]))


# imprimir_solucao([0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1])


def fitness_function(solucao):
    custo = 0
    soma_espaco = 0
    for i in range(len(solucao)):
        if solucao[i] == 1:
            custo += produtos[i][2]
            soma_espaco += produtos[i][1]
    if soma_espaco > espaco_disponivel:
        custo = 1
    return custo


# fitness_function([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1])


fitness = mlrose.CustomFitness(fitness_function)
problema = mlrose.DiscreteOpt(length=14,
                              fitness_fn=fitness,
                              maximize=True,
                              max_val=2)

# Algoritmo Hill Climb
melhor_solucao_hill, melhor_custo_hill = mlrose.hill_climb(problema)
melhor_solucao_hill, melhor_custo_hill

print('-----> Essa é o resultado do algoritmo Hill Climb')
imprimir_solucao(melhor_solucao_hill)
print(f'R$ {format(fitness_function(melhor_solucao_hill),".2f")}')

# Algoritmo Simulated Annealing
melhor_solucao_sian, melhor_custo_sian = mlrose.simulated_annealing(problema)
melhor_solucao_sian, melhor_custo_sian

print('-----> Essa é o resultado do algoritmo Simulated Annealing')
imprimir_solucao(melhor_solucao_sian)
print(f'R$ {format(fitness_function(melhor_solucao_sian),".2f")}')

# Algoritmo Genetico
melhor_solucao_gen, melhor_custo_gen = mlrose.genetic_alg(problema,
                                                          pop_size=500,
                                                          mutation_prob=0.2)
melhor_solucao_gen, melhor_custo_gen

print('-----> Essa é o resultado do algoritmo Genético')
imprimir_solucao(melhor_solucao_gen)
print(f'R$ {format(fitness_function(melhor_solucao_gen),".2f")}')
