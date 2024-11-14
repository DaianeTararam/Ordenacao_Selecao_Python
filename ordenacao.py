def buscaMenor(array):
    menor = array[0]
    menor_indice = 0
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice

def ordenacaoSelecao(array):
    novoArray = []
    for i in range(len(array)):
        menor = buscaMenor(array)
        novoArray.append(array.pop(menor))
    return novoArray

print (ordenacaoSelecao([6,7,20,5,1,2,0]))
