import csv

# Classificação de risco
colunas = ['Historico de credito', 'Divida', 'Garantias',
           'Renda anual', 'Risco']
classificacao = [
    ['Ruim', 'Alta', 'Nenhuma', '< 15000', 'Alto'],
    ['Desconhecida', 'Alta', 'Nenhuma', '>= 15000 a <= 35000', 'Alto'],
    ['Desconhecida', 'Baixa', 'Nenhuma', '>= 15000 a <= 35000', 'Moderado'],
    ['Desconhecida', 'Baixa', 'Nenhuma', '< 15000', 'Alto'],
    ['Desconhecida', 'Baixa', 'Nenhuma', '> 35000', 'Baixo'],
    ['Desconhecida', 'Baixa', 'Adequada', '> 35000', 'Baixo'],
    ['Ruim', 'Baixa', 'Nenhuma', '< 15000', 'Alto'],
    ['Ruim', 'Baixa', 'Adequada', '> 35000', 'Moderado'],
    ['Boa', 'Baixa', 'Nenhuma', '> 35000', 'Baixo'],
    ['Boa', 'Alta', 'Adequada', '> 35000', 'Baixo'],
    ['Boa', 'Alta', 'Nenhuma', '< 15000', 'Alto'],
    ['Boa', 'Alta', 'Nenhuma', '>= 15000 a <= 35000', 'Moderado'],
    ['Boa', 'Alta', 'Nenhuma', '> 35000', 'Baixo'],
    ['Ruim', 'Alta', 'Nenhuma', '>= 15000 a <= 35000', 'Alto']
]

# Escrevendo arquivo especificado CSV
with open('classificacao.csv', 'w', newline='',
          encoding='UTF-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=';')
    escritor.writerow(colunas)
    escritor.writerows(classificacao)

# Lendo arquivo csv e criando objeto para
with open('classificacao.csv', 'r', newline='',
          encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    tabela_classificacao = []
    for linha in leitor:
        tabela_classificacao.append(linha)
    print(tabela_classificacao)

# Desenpacotando o arquivo csv
novas_colunas, *novo_objeto = tabela_classificacao
print(novas_colunas)
print('[', *novo_objeto, sep='\n  ', end='\n]')
