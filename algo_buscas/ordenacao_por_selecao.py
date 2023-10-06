def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
        return menor_indice


def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(1, len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


array = [5, 1, 3, 4, 2]


resultado = ordenacaoPorSelecao(array)
