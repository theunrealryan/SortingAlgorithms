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
            a[j+1] = a[j]
            j -= 1
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

# --- Plotagem com Big O ---
def plotar_com_big_o(tamanhos, medidos):
    """
    Para cada algoritmo em `medidos`, plota:
      - a curva empírica (marcadores sólidos)
      - a curva teórica Big O correspondente (linha tracejada),
        normalizada para coincidir no último ponto.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    n = np.array(tamanhos, dtype=float)

    # mapeamento nome -> (função_complexidade, etiqueta)
    complexidades = {
        "Merge Sort": (lambda n: n * np.log2(n), "O(n log n)"),
        "Insertion Sort": (lambda n: n**2,           "O(n²)"),
        "Bubble Sort":    (lambda n: n**2,           "O(n²)"),
    }

    # escolher uma paleta para cores repetíveis
    cores = plt.rcParams['axes.prop_cycle'].by_key()['color']

    for idx, (nome, tempos) in enumerate(medidos.items()):
        tempos = np.array(tempos, dtype=float)
        plt.plot(n, tempos,
                 marker='o', linestyle='-',
                 color=cores[idx],
                 label=f"{nome} (empírico)")

        # se tivermos uma complexidade definida, plota teórica
        if nome in complexidades:
            f_comp, label_comp = complexidades[nome]
            vals = f_comp(n)
            # fator de escala para coincidir no último ponto
            scale = tempos[-1] / vals[-1]
            teoc = vals * scale
            plt.plot(n, teoc,
                     linestyle='--',
                     color=cores[idx],
                     label=f"{nome} ({label_comp})")

    ax.set_xlabel("Tamanho da entrada (n)")
    ax.set_ylabel("Tempo médio (s)")
    ax.set_title("Desempenho Empírico vs. Notação Big O")
    ax.grid(True, linestyle=':')
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
    ent = input("Tamanhos (ex: 5000,10000,20000): ")
    try:
        ts = [int(x) for x in ent.split(',') if x.strip()]
    except:
        ts = [1000, 5000, 10000]
    mn = int(input("Mínimo elemento: "))
    mx = int(input("Máximo elemento: "))
    if mn > mx: mn, mx = mx, mn
    reps = max(1, int(input("Repetições: ")))
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

    print("\n--- Medições ---")
    resultados = comparar_algoritmos(selecionados, tamanhos, minimo, maximo, reps)

    print("\n--- Gráfico Empírico vs. Big O ---")
    plotar_com_big_o(tamanhos, resultados)

if __name__ == "__main__":
    main()