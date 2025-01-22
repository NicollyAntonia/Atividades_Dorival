"""
#marget sort




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
"""
#Busca linear
def busca_linear(loucura3, valor):
    for i in range(len(loucura3)):  #Percorre toda a lista procurando o elemento
        if loucura3[i] == valor:  #Compara o elemento da lista com o valor procurado
            return i  #Da o índice/posição do valor encontrado
    return -1  #Da -1 se o valor não for encontrado

loucura3 = [10, 25, 30, 42, 50, 65, 80, 100]
valor = 42
print(f"\nSua busca está no indice : {busca_linear(loucura3, valor)}")

#Busca binária


#Calculo de algoritmo e complexidade




