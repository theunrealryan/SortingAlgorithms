import random
import time
import statistics

#função para gerar listas de dados aleatórios
def gerar_lista_aleatoria(tamanho, minimo, maximo):
    
  lista = []
  for i in range(tamanho):
    numero_aleatorio = random.randint(minimo, maximo)
    lista.append(numero_aleatorio)
  return lista
#definir tamanho e valores da lista aleatória
tamanho = 10000
minimo = 1
maximo = 10000

#função algoritmo de ordenação merge sort
def merge_sort(lista):

  if len(lista) <= 1:
    return lista

  meio = len(lista) // 2
  esquerda = merge_sort(lista[:meio])
  direita = merge_sort(lista[meio:])

  return merge(esquerda, direita)

def merge(lista_esquerda, lista_direita):

  lista_ordenada = []
  i, j = 0, 0

  while i < len(lista_esquerda) and j < len(lista_direita):
    if lista_esquerda[i] <= lista_direita[j]:
      lista_ordenada.append(lista_esquerda[i])
      i += 1
    else:
      lista_ordenada.append(lista_direita[j])
      j += 1

  lista_ordenada += lista_esquerda[i:]
  lista_ordenada += lista_direita[j:]

  return lista_ordenada

#repetir o merge sort n vezes, cada vez com uma lista aleatória diferente
vetor_tempo_merge_sort = []
for i in range(100):
  lista_aleatoria = gerar_lista_aleatoria(tamanho, minimo, maximo)
  tempo_inicial_merge_sort = time.time()
  lista_ordenada = merge_sort(lista_aleatoria)
  tempo_final_merge_sort = time.time()
  vetor_tempo_merge_sort.append(tempo_final_merge_sort-tempo_inicial_merge_sort)
#printar a média, moda, mediana, variância e desvio padrão do tempo de execução do merge sort
print(f'Merge sort\n Média: {statistics.mean(vetor_tempo_merge_sort)}\n Moda: {statistics.mode(vetor_tempo_merge_sort)}\n Mediana: {statistics.median(vetor_tempo_merge_sort)}\n Variância: {statistics.pvariance(vetor_tempo_merge_sort)}\n Desvio Padrão: {statistics.pstdev(vetor_tempo_merge_sort)}')

#função algortimo de ordenação insertion sort
def insertion_sort(lista):
  
  for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1

    while j >= 0 and lista[j] > chave:
      lista[j + 1] = lista[j]
      j -= 1

    lista[j + 1] = chave

  return lista

#repetir o insertion sort n vezes, cada vez com uma lista aleatória diferente
vetor_tempo_insertion_sort = []
for i in range(100):
  lista_aleatoria = gerar_lista_aleatoria(tamanho, minimo, maximo)
  tempo_inicial_insertion_sort = time.time()
  lista_ordenada = insertion_sort(lista_aleatoria)
  tempo_final_insertion_sort = time.time()
  vetor_tempo_insertion_sort.append(tempo_final_insertion_sort-tempo_inicial_insertion_sort) 
#printar a média, moda, mediana, variância e desvio padrão do tempo de execução do insertion sort
print(f'Insertion Sort\n Média: {statistics.mean(vetor_tempo_insertion_sort)}\n Moda: {statistics.mode(vetor_tempo_insertion_sort)}\n Mediana: {statistics.median(vetor_tempo_insertion_sort)}\n Variância: {statistics.pvariance(vetor_tempo_insertion_sort)}\n Desvio Padrão: {statistics.pstdev(vetor_tempo_insertion_sort)}')

#função algortimo de ordenação bubble sort
def bubble_sort(lista):
  for i in range(len(lista) - 1):
    for j in range(len(lista) - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  return lista

#repetir o bubble sort n vezes, cada vez com uma lista aleatória diferente
vetor_tempo_bubble_sort = []
for i in range(100):
  lista_aleatoria = gerar_lista_aleatoria(tamanho, minimo, maximo)
  tempo_inicial_bubble_sort = time.time()
  lista_ordenada = bubble_sort(lista_aleatoria)
  tempo_final_bubble_sort = time.time()
  vetor_tempo_bubble_sort.append(tempo_final_bubble_sort - tempo_inicial_bubble_sort)
#printar a média, moda, mediana, variância e desvio padrão do tempo de execução do bubble sort
print(f'Bubble Sort\n Média: {statistics.mean(vetor_tempo_bubble_sort)}\n Moda: {statistics.mode(vetor_tempo_bubble_sort)}\n Mediana: {statistics.median(vetor_tempo_bubble_sort)}\n Variância: {statistics.pvariance(vetor_tempo_bubble_sort)}\n Desvio Padrão: {statistics.pstdev(vetor_tempo_bubble_sort)}')