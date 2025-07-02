import random
import time
import statistics
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Geração de dados ---
def gerar_lista_aleatoria(n, minimo, maximo):
    """Gera lista de inteiros aleatórios em [minimo, maximo]."""
    return [random.randint(minimo, maximo) for _ in range(n)]

# --- Algoritmos de ordenação ---
def merge_sort(a):
    """Merge Sort clássico (O(n·log n))."""
    if len(a) <= 1:
        return a
    m = len(a) // 2
    left = merge_sort(a[:m])
    right = merge_sort(a[m:])
    return merge(left, right)

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

# --- Plotagem combinada (com ajuste adequado de escalas) ---
def plotar_combinado(tamanhos, medidos):
    fig, ax = plt.subplots(figsize=(10, 6))
    n = np.array(tamanhos, dtype=float)

    # Estilos para os algoritmos
    estilos = {
        "Merge Sort":     {"marker": "o", "linestyle": "-",  "color": "C0", "linewidth": 2},
        "Insertion Sort": {"marker": "s", "linestyle": "-",  "color": "C1", "linewidth": 2},
        "Bubble Sort":    {"marker": "^", "linestyle": "-",  "color": "C2", "linewidth": 2},
    }

    # Plotagem das curvas de tempos empíricos
    for nome, tempos in medidos.items():
        tempos = np.array(tempos, dtype=float)
        style = estilos.get(nome, {})
        ax.plot(n, tempos,
                marker=style["marker"],
                linestyle=style["linestyle"],
                color=style["color"],
                linewidth=style["linewidth"],
                label=f"{nome} (empírico)")

    # Funções de complexidade teórica
    teorica = {
        "Merge Sort":     lambda n: n * np.log2(n),
        "Insertion Sort": lambda n: n**2,
        "Bubble Sort":    lambda n: n**2
    }

    # Plotando as curvas teóricas (O(n log n) e O(n^2))
    for nome, f_comp in teorica.items():
        vals = f_comp(n)
        scale = np.max(medidos[nome]) / np.max(vals)  # Escala para coincidir com os valores empíricos
        ax.plot(n, vals * scale, linestyle='--', color=estilos[nome]["color"], label=f"{nome} (teórica)")

    # Configuração do gráfico
    ax.set_xlabel("Tamanho da entrada (n)")
    ax.set_ylabel("Tempo médio de execução (s)")
    ax.set_title("Desempenho Empírico de Algoritmos de Ordenação")
    
    # Ajuste da escala logarítmica para evidenciar a diferença entre n^2 e n*log(n)
    ax.set_yscale('log')  # Escala logarítmica para mostrar diferenças de crescimento

    ax.grid(True, which='both', linestyle=':')

    # Usando FuncFormatter para remover notação científica no eixo Y
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.6f}s"))
    
    ax.legend()
    plt.tight_layout()
    plt.show()

# --- Interação com usuário ---
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
        if not ts:
            raise ValueError
    except ValueError:
        ts = [1000, 2000, 4000]
    mn = int(input("Valor mínimo dos elementos: "))
    mx = int(input("Valor máximo dos elementos: "))
    if mn > mx:
        mn, mx = mx, mn
    rep = input("Repetições por tamanho [5]: ").strip()
    reps = int(rep) if rep.isdigit() else 5
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

    print(f"\nExecutando {reps} repetições por tamanho...\n")
    resultados = comparar_algoritmos(selecionados, tamanhos, minimo, maximo, reps)

    print("\n--- Gerando gráfico combinado ---")
    plotar_combinado(tamanhos, resultados)

if __name__ == "__main__":
    main()