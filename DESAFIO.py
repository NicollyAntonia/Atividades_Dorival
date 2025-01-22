
#marget sort(não entendi direito dorival)
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        result.append(left[i] if left[i] < right[j] else right[j])
        i, j = (i + 1, j) if left[i] < right[j] else (i, j + 1)
    return result + left[i:] + right[j:]
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))



#insert
def insert_sort(loucura):#definindo a função e chamando o insert paraa organização
    for i in range(1,len(loucura)): # Inicia a iteração a partir do segundo elemento e inicia o loop em 1 já que a primeira posição e considerada ordenada
        novo=loucura[i]  # O elemento a ser inserido na parte ordenada da lista
        j=i-1# A posição inicial para verificar os elementos à esquerda de 'novo'
        while j>=0 and loucura[j]>novo: # Enquanto j for maior ou igual a 0 e o valor em loucura[j] for maior que 'n
            loucura[j+1]=loucura[j] # Move o elemento para a direita
            j-=1  # Desce o índice 'j' para comparar com o próximo elemento à esquerda

        loucura[j+1]=novo# Insere o 'novo' na posição correta dentro da parte ordenada

loucura=[5,8,9,4,9,6,29,44,88,99,5479893,0]#lista a ser ordenada
insert_sort(loucura)#reordenando
print(f"\nSua lista com insert sort:{loucura}")#mostrando pro usuário


#bubble sort CERTO
def bubble_sort(loucura2):
    elementos = len(loucura2) - 1  # Subtração de 1 pois a comparação é feita entre índice i e i+1
    ordenado = False
    while not ordenado:
        ordenado = True  # Assume que a lista está ordenada até que se prove o contrário
        for i in range(elementos):
            if loucura2[i] > loucura2[i + 1]:
                loucura2[i], loucura2[i + 1] = loucura2[i + 1], loucura2[i]  # Troca os elementos
                ordenado = False  # Se houver uma troca, a lista não está ordenada
                print(loucura2)
    return lista

lista = [9, 7, 8, 3, 1, 0, 20, 21, 22, 45, 69]
print(f"Lista ordenada: {bubble_sort(lista)}")

#Busca linear
def busca_linear(loucura3, valor):
    for i in range(len(loucura3)):  #Percorre toda a lista procurando o elemento
        if loucura3[i] == valor:  #Compara o elemento da lista com o valor procurado
            return i  #Da o índice/posição do valor encontrado
    return -1  #Da -1 se o valor não for encontrado

loucura3 = [10, 25, 30, 42, 50, 65, 80, 100]
valor = 42
print(f"\nSua busca está no indice : {busca_linear(loucura3, valor)}")

"""
#Busca binária
A busca binária é tipo um truque ninja pra encontrar algo rápido numa lista ordenada. 
Em vez de ficar procurando um por um (que nem a busca normal), ela corta a lista no meio e foca só na metade que tem o valor que você quer.
Isso faz com que seja bem mais rápido, principalmente quando a lista é gigantesca.
Mas tem que ser uma lista ordenada. Se não, não dá pra usar .


#Calculo de algoritmo e complexidade
Quando a gente fala de cálculo de complexidade de algoritmo, a gente tá basicamente tentando entender quanto tempo ou espaço o algoritmo vai consumir quando a entrada (o tamanho dos dados) aumenta. 
E, pra isso, usamos uma parada chamada notação Big O (ou O grande), que é tipo uma forma de medir a velocidade do algoritmo. 
Então, a ideia é saber quanto o tempo vai aumentar conforme a quantidade de dados cresce.
Como calcula????
Tambem não entendi só sei que tem função de 1 grau......lágrimas
"""



