#!/usr/bin/env python3
"""
Comparação didática de algoritmos de ordenação em Python,
mantendo Merge Sort inalterado e exibindo para Insertion e Bubble Sort
ambas as curvas—empírica e teórica O(n²)—com linhas contínuas.
"""

import random
import time
import statistics
import numpy as np
import matplotlib.pyplot as plt

# --- Geração de dados ---
def gerar_lista_aleatoria(n, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(n)]

# --- Ordenações ---
def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    return merge(merge_sort(a[:m]), merge_sort(a[m:]))

def merge(l, r):
    res, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
    res.extend(l[i:]); res.extend(r[j:])
    return res

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]; j -= 1
        a[j+1] = key
    return a

def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# --- Medição de tempo ---
def medir_tempo(func, n, minimo, maximo, reps):
    tempos = []
    for _ in range(reps):
        lst = gerar_lista_aleatoria(n, minimo, maximo)
        start = time.perf_counter()
        func(lst.copy())
        end = time.perf_counter()
        tempos.append(end - start)
    return statistics.mean(tempos)

def comparar_algoritmos(algos, tamanhos, minimo, maximo, reps):
    resultados = {nome: [] for nome in algos}
    for n in tamanhos:
        print(f"Medindo n = {n}...")
        for nome, func in algos.items():
            t = medir_tempo(func, n, minimo, maximo, reps)
            resultados[nome].append(t)
        print("  OK")
    return resultados

# --- Plotagem com curvas teóricas contínuas para O(n²) ---
def plotar_empirico_on2(tamanhos, medidos):
    """
    Plota curvas empíricas de Merge, Insertion e Bubble Sort,
    e para Insertion e Bubble exibe também a curva O(n²)
    com linha contínua e leve transparência.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    n = np.array(tamanhos, dtype=float)

    estilos = {
        "Merge Sort":     {"marker": "o", "color": "C0"},
        "Insertion Sort": {"marker": "s", "color": "C1"},
        "Bubble Sort":    {"marker": "^", "color": "C2"},
    }

    # Plot empírico
    for nome, tempos in medidos.items():
        tempos = np.array(tempos, dtype=float)
        style = estilos[nome]
        ax.plot(n, tempos,
                marker=style["marker"],
                linestyle='-',
                color=style["color"],
                linewidth=2,
                label=f"{nome} (empírico)")

    # Plot O(n²) para Insertion e Bubble, contínuo
    for nome in ("Insertion Sort", "Bubble Sort"):
        if nome in medidos:
            tempos = np.array(medidos[nome], dtype=float)
            # referência teórica y = k * n^2
            k = tempos[-1] / (n[-1]**2)
            ref = k * n**2
            style = estilos[nome]
            ax.plot(n, ref,
                    marker=None,
                    linestyle='-',
                    color=style["color"],
                    linewidth=2,
                    alpha=0.6,
                    label=f"{nome} (O(n²))")

    ax.set_xlabel("Tamanho da entrada (n)")
    ax.set_ylabel("Tempo médio de execução (s)")
    ax.set_title("Desempenho Empírico e O(n²) para Insertion & Bubble Sort")
    ax.set_yscale('log')
    ax.grid(True, which='both', linestyle=':')
    ax.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

# --- Interação ---
def solicitar_algoritmos(disponiveis):
    print("Selecione algoritmos (Enter = todos):")
    for chave, (nome, _) in disponiveis.items():
        print(f"  {chave}) {nome}")
    entrada = input("Ex: 1,3 → ")
    sel = {}
    for token in entrada.split(','):
        chave = token.strip()
        if chave in disponiveis:
            nome, func = disponiveis[chave]
            sel[nome] = func
    if not sel:
        sel = {nome: func for nome, func in disponiveis.values()}
    return sel

def solicitar_parametros():
    try:
        ts = [int(x) for x in input("Tamanhos (ex: 1000,2000,4000): ").split(',')]
        if not ts: raise ValueError
    except ValueError:
        ts = [1000, 2000, 4000]
    mn = int(input("Valor mínimo dos elementos: "))
    mx = int(input("Valor máximo dos elementos: "))
    if mn > mx: mn, mx = mx, mn
    reps = max(1, int(input("Repetições por tamanho: ")))
    return ts, mn, mx, reps

def main():
    disponiveis = {
        "1": ("Merge Sort", merge_sort),
        "2": ("Insertion Sort", insertion_sort),
        "3": ("Bubble Sort", bubble_sort),
    }
    selecionados = solicitar_algoritmos(disponiveis)

    print("\n--- Parâmetros da lista ---")
    tamanhos, minimo, maximo, reps = solicitar_parametros()

    print("\n--- Executando medições ---")
    resultados = comparar_algoritmos(selecionados, tamanhos, minimo, maximo, reps)

    print("\n--- Gerando gráfico ---")
    plotar_empirico_on2(tamanhos, resultados)

if __name__ == "__main__":
    main()