import random
import time
import math
import statistics
import matplotlib.pyplot as plt

# --- Bogosort e utilitários ---

def is_sorted(arr):
    """Verifica se a lista está ordenada."""
    return all(arr[i] >= arr[i-1] for i in range(1, len(arr)))

def bogo_sort(arr):
    """Embaralha até que a lista fique ordenada."""
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def generate_random_array(n, min_val, max_val):
    """Gera uma lista de inteiros aleatórios em [min_val, max_val]."""
    return [random.randint(min_val, max_val) for _ in range(n)]

# --- Parâmetros fixos para o benchmark de picos ---
size_fixed = 10       # n fixo
min_val    = 1
max_val    = 100
num_trials = 20       # número de tentativas em n = size_fixed

# --- 1) Coleta de picos em n = size_fixed ---
trial_times = []
for _ in range(num_trials):
    arr = generate_random_array(size_fixed, min_val, max_val)
    t0 = time.perf_counter()
    bogo_sort(arr)
    t1 = time.perf_counter()
    trial_times.append(t1 - t0)

# Média em n=10
avg_fixed = statistics.mean(trial_times)
# Ops teóricas em n=10: n * n!
ops_fixed = size_fixed * math.factorial(size_fixed)
# Escala para converter ops → segundos (aqui resulta avg_fixed)
scale_fixed = avg_fixed / ops_fixed

# --- 2) Coleta de médias em vários n ---
sizes     = list(range(2, 9))  # de 2 até 8
avg_times = []
for n in sizes:
    runs = []
    for _ in range(num_trials):
        arr = generate_random_array(n, min_val, max_val)
        t0 = time.perf_counter()
        bogo_sort(arr)
        t1 = time.perf_counter()
        runs.append(t1 - t0)
    avg_times.append(statistics.mean(runs))

# Ops teóricas para cada n em sizes
ops_sizes = [n * math.factorial(n) for n in sizes]
# Escala escolhida para que o ponto em n=8 coincida
scale_sizes = avg_times[-1] / ops_sizes[-1]
# Curva teórica normalizada
theoretical_sizes = [op * scale_sizes for op in ops_sizes]

# --- Plotagem final com subplots ---

fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(9, 11))

# Gráfico 1: Picos em n = 10
ax0.plot(
    range(1, num_trials+1),
    trial_times,
    marker='o', linestyle='-',
    color='C0',
    label='Bogosort (medido)'
)
# Linha horizontal na média teórica exata (hlines)
ax0.hlines(
    y=avg_fixed,
    xmin=1, xmax=num_trials,
    colors='C1',
    linestyles='--',
    label=r'Teoria: $n\times n!$ (calibrada)'
)
ax0.set_title(f'Bogosort (n={size_fixed}): Picos por tentativa')
ax0.set_xlabel('Tentativa')
ax0.set_ylabel('Tempo (s)')
ax0.set_yscale('log')                 # log para evidenciar variações
ax0.grid(True, which='both', linestyle=':')
ax0.legend()

# Gráfico 2: Tempo médio vs tamanho
ax1.plot(
    sizes,
    avg_times,
    marker='o', linestyle='-',
    color='C0',
    label='Média empírica'
)
ax1.plot(
    sizes,
    theoretical_sizes,
    marker='x', linestyle='--',
    color='C1',
    label=r'Teoria: $n\times n!$'
)
ax1.set_title('Bogosort: Tempo médio vs Complexidade teórica')
ax1.set_xlabel('Tamanho da entrada (n)')
ax1.set_ylabel('Tempo médio (s)')
ax1.set_yscale('log')                 # log para mostrar crescimento fatorial
ax1.grid(True, which='both', linestyle=':')
ax1.legend()

plt.tight_layout()
plt.show()