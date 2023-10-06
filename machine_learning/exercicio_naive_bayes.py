import csv


# PARA BUSCAS E SEPARAR DADOS EM UM ARQUIVO TXT
with open('classificacao.csv', 'r', newline='',
          encoding='UTF-8') as arquivo_csv:
    risco_de_credito = {}
    leitor = csv.reader(arquivo_csv, delimiter=';')
    for linha in arquivo_csv:
        historico, divida, garantias, renda, risco = linha.split(',')
        risco_de_credito.setdefault((risco), [])
        risco_de_credito[(risco)].append((historico, divida, garantias, renda))
        print(risco_de_credito)
