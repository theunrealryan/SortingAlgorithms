````markdown
## Projeto SortingAlgorithms

Implementação em **Python** de três algoritmos clássicos de ordenação—**Merge Sort**, **Insertion Sort** e **Bubble Sort**—com geração de listas aleatórias para fins de avaliação empírica. O código foi desenvolvido originalmente durante a disciplina de **Estatística Aplicada à Informática** (2º semestre de 2024) no Bacharelado em Engenharia de Software da Universidade do Estado do Pará (UEPA) e posteriormente aprimorado para a palestra:

> **Análise de Complexidade e Algoritmos de Ordenação em Python: Big O na Prática**  
> Python Norte · Julho de 2025 :contentReference[oaicite:0]{index=0}

---

## 📂 Estrutura do Repositório

- **README.md**  
  Descrição do projeto e instruções de uso :contentReference[oaicite:1]{index=1}  
- **algoritmos de ordenação merge sort, insertion sort, bubble sort.py**  
  Script principal contendo:
  - Geração de listas aleatórias  
  - Implementações de Merge Sort, Insertion Sort e Bubble Sort  
  - Medição de tempo de execução para diferentes tamanhos de entrada :contentReference[oaicite:2]{index=2}  

**Linguagem:** Python (100%) :contentReference[oaicite:3]{index=3}  
**Commits até o momento:** 4 :contentReference[oaicite:4]{index=4}  
**Stars:** 1 :contentReference[oaicite:5]{index=5}  

---

## 🚀 Funcionalidades Principais

1. **Geração de Listas Aleatórias**  
   Parâmetros de tamanho, valor mínimo e valor máximo configuráveis pelo usuário.

2. **Algoritmos de Ordenação**  
   - **Merge Sort**: divisão e conquista, \(O(n\log n)\)  
   - **Insertion Sort**: comparações e deslocamentos, \(O(n^2)\)  
   - **Bubble Sort**: trocas sucessivas de pares, \(O(n^2)\)

3. **Medição de Desempenho**  
   Uso de `time.perf_counter()` para capturar o tempo médio de execução em várias repetições e diferentes tamanhos de entrada.

---

## 💻 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/theunrealryan/SortingAlgorithms.git
   cd SortingAlgorithms
````

2. (Opcional) Crie um ambiente virtual e ative-o:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Execute o script:

   ```bash
   python "merge-insertion-bubble.py"
   ```
4. Siga as instruções interativas para:

   * Escolher algoritmo(s) a executar
   * Definir tamanhos de lista, intervalo de valores
   * Especificar número de repetições

---

## 📝 Evolução

* **2024.1 (UEPA)**
  Base acadêmica: estudo de estatística aplicada à comparação de algoritmos.

* **2025.1 (Python Norte)**
  Aprimoramentos para workshop:

  * Seleção interativa de algoritmos
  * Plotagem de gráficos empíricos vs. curvas teóricas de Big O
  * Estudos de caso com Bogosort e análise de picos de execução

---

## 🤝 Contribuições

Pull requests são bem-vindos! Sugerimos:

* Adicionar novos algoritmos (QuickSort, HeapSort, etc.).
* Melhorar visualizações gráficas.
* Incluir testes automatizados e documentação adicional.

---

### Licença

Este projeto está sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para detalhes.