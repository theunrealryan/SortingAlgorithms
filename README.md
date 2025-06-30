# SortingAlgorithms

## Desenvolvimento

Este repositório foi iniciado como trabalho prático da disciplina **Estatística Aplicada à Informática** (2º semestre do curso em 2024.1) de Bacharelado em Engenharia de Software — Universidade do Estado do Pará (UEPA).  
Em 2025 foi expandido e aprimorado para a palestra **“Análise de Complexidade e Algoritmos de Ordenação em Python: Big O na Prática”**, apresentada no evento **Python Norte** (julho/2025), ganhando:

* interface 100 % interativa (CLI) para escolher algoritmos e parâmetros;  
* coleta de tempos médios com múltiplas repetições;  
* gráficos empíricos × curvas teóricas ( _O(n log n)_ , _O(n²)_ , _n·n!_ …);  
* comparativo especiail para o Bogosort de complexidade fatorial.

---

## Fundamentos teóricos

* **Notação Big O** descreve limite assintótico superior de tempo ou espaço.
* `O(n log n)` surge em algoritmos que dividem dados recursivamente e depois mesclam (caso do Merge Sort).
* `O(n²)` caracteriza métodos baseados em comparação par-a-par — pivotando ou deslocando itens — em cada passo.
* **Bogosort** exibe complexidade esperada `Θ(n · n!)` porque existem `n!` permutações possíveis e apenas uma está ordenada.

Essas classes são traçadas nos gráficos para evidenciar quão bem (ou mal!) o comportamento empírico segue a teoria.

---

## Sobre o projeto

| Algoritmo       | Classe Big O | Observações |
|-----------------|--------------|-------------|
| Merge Sort      | `O(n log n)` | estratégia dividir-e-conquistar; estável; bom para arquivos grandes |
| Insertion Sort  | `O(n²)`      | excelente para listas quase ordenadas e pequeno _n_  |
| Bubble Sort     | `O(n²)`      | simples, mas um dos mais lentos em caso médio |
| **Bogosort**    | `Θ(n · n!)`  | embaralha até ordenar; usado apenas para demonstração de “código terrível” |

---

## Estrutura do Projeto

```
SortingAlgorithms/
├─ README.md                     # documentação e instruções de uso
├─ merge-insertion-bubble.py     # script CLI para comparar Merge, Insertion e Bubble Sort
├─ bogosort.py                   # benchmark e plotagem dedicados ao Bogosort
└─ (venv/ e .venv/)              # ambientes virtuais

````

---

## Instalação rápida

```bash
git clone https://github.com/theunrealryan/SortingAlgorithms.git
cd SortingAlgorithms
python3 -m venv venv && source venv/bin/activate   # opcional
pip install numpy matplotlib
````

---

## Executando **e interagindo** com `merge-insertion-bubble.py`

### 1. Inicie o script

```bash
python merge-insertion-bubble.py
```

### 2. Escolha os algoritmos

```
Selecione algoritmos (Enter = todos):
  1) Merge Sort
  2) Insertion Sort
  3) Bubble Sort
Ex: 1,3 →
```

* **Enter vazio** roda **todos**.
* `1,3` roda apenas Merge Sort e Bubble Sort.

### 3. Defina os tamanhos de entrada

```
Tamanhos (ex: 1000,5000,10000):
```

Digite uma lista de *n*. O script aceita qualquer quantidade de valores inteiros; caso o formato falhe, usa `[1000, 5000, 10000]` como padrão.

### 4. Configure o intervalo de valores

```
Mínimo elemento: 0
Máximo elemento: 1000
```

Esses limites definem `random.randint(min,max)` para gerar cada elemento.

### 5. Informe o número de repetições

```
Repetições: 5
```

Cada algoritmo será executado 5 × por tamanho de lista; usamos a média para reduzir variação estatística.

### 6. Acompanhe o terminal

```
Medindo n = 5000...
  Merge Sort    : 0.0123 s
  Bubble Sort   : 1.0345 s
```

Para cada *n* você recebe o tempo médio já formatado.

### 7. Analise o gráfico (Matplotlib)

Uma janela se abre mostrando:

* **Linhas sólidas** – tempos empíricos por algoritmo.
* **Linhas tracejadas** – curvas teóricas normalizadas:

  * *Merge Sort* usa `n·log₂n`;
  * *Insertion* e *Bubble* usam `n²`.

> Os traços coincidem no último ponto para facilitar a leitura comparativa.

### 8. Experimentos sugeridos

| Experimento              | Configuração                          | Insight                                                                   |
| ------------------------ | ------------------------------------- | ------------------------------------------------------------------------- |
| **Lista quase ordenada** | `Mín=1, Máx=10` + `tamanhos pequenos` | Perceba *Insertion Sort* em `O(n)` no melhor caso ([en.wikipedia.org][2]) |
| **Stress Bubble**        | `tamanhos altos` (≥ 20 000)           | Observe crescimento quadrático tornar-se proibitivo                       |
| **Bogosort isolado**     | `python bogo_benchmark.py`            | Compare picos individuais (n=10) vs. curva média `n · n!` em escala log   |

---

## Licença

Código sob **MIT License** — consulte o arquivo [`LICENSE`](LICENSE).
