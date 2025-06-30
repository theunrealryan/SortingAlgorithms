import random
import time
import math
import statistics
import matplotlib.pyplot as plt

# --- Bogosort ---
def is_sorted(arr):
    return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def generate_random_array(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]

# --- Parâmetros fixos ---
size_fixed = 10      # n para o gráfico de picos
min_val    = 1
max_val    = 100
num_trials = 20      # execuções em n = size_fixed

# --- Coleta de tempos por tentativa (n fixo) ---
trial_times = []
for _ in range(num_trials):
    arr = generate_random_array(size_fixed, min_val, max_val)
    t0 = time.perf_counter()
    bogo_sort(arr)
    t1 = time.perf_counter()
    trial_times.append(t1 - t0)

avg_fixed = statistics.mean(trial_times)
ops_fixed = size_fixed * math.factorial(size_fixed)
scale_fixed = avg_fixed / ops_fixed
theoretical_fixed = [ops_fixed * scale_fixed] * num_trials

# --- Coleta de tempos médios em vários n ---
sizes = list(range(2, 9))  # n de 2 a 8
avg_times = []
for n in sizes:
    times_n = []
    for _ in range(num_trials):
        arr = generate_random_array(n, min_val, max_val)
        t0 = time.perf_counter()
        bogo_sort(arr)
        t1 = time.perf_counter()
        times_n.append(t1 - t0)
    avg_times.append(statistics.mean(times_n))

ops_sizes = [n * math.factorial(n) for n in sizes]
scale_sizes = avg_times[-1] / ops_sizes[-1]
theoretical_sizes = [op * scale_sizes for op in ops_sizes]

# --- Plotagem com dois subplots ---
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(8, 10))

# 1) Picos por tentativa em n = size_fixed
ax0.plot(range(1, num_trials + 1),
         trial_times,
         marker='o',
         linestyle='-',
         label='Bogosort (medido)')
ax0.plot(range(1, num_trials + 1),
         theoretical_fixed,
         linestyle='--',
         color='C1',
         label=r'Teoria $n \times n!$')
ax0.set_title(f'Bogosort (n={size_fixed}): Picos por tentativa')
ax0.set_xlabel('Tentativa')
ax0.set_ylabel('Tempo (s)')
ax0.grid(True, linestyle=':')
ax0.legend()

# 2) Média empírica vs. teoria em função de n
ax1.plot(sizes,
         avg_times,
         marker='o',
         linestyle='-',
         label='Média empírica')
ax1.plot(sizes,
         theoretical_sizes,
         marker='x',
         linestyle='--',
         label=r'Teoria $n \times n!$')
ax1.set_title('Bogosort: Tempo médio vs. Complexidade teórica')
ax1.set_xlabel('Tamanho da entrada (n)')
ax1.set_ylabel('Tempo médio (s)')
ax1.set_yscale('log')  # para acomodar rápido crescimento
ax1.grid(True, which='both', linestyle=':')
ax1.legend()

plt.tight_layout()
plt.show()