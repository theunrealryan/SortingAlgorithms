## 🎯 Sobre o Projeto

Este repositório oferece uma ferramenta didática e interativa para explorar a **complexidade de algoritmos** de forma visual e prática. Ele foi criado para demonstrar como a **Notação Big O** não é apenas teoria, mas uma descrição precisa do desempenho de algoritmos no mundo real.

Aqui, você pode comparar algoritmos clássicos como **Merge Sort**, **Insertion Sort** e **Bubble Sort**, e até mesmo o infame e cômico **Bogo Sort**, para entender o que torna um código eficiente ou desastrosamente lento.

### Histórico
- **Origem (2024.1):** Iniciado como trabalho prático da disciplina de *Estatística Aplicada à Informática* na graduação em Engenharia de Software da Universidade do Estado do Pará (UEPA).
- **Expansão (07/2025):** Aprimorado para a palestra *“Análise de Complexidade e Algoritmos de Ordenação em Python: Big O na Prática”* no evento **Python Norte**, ganhando novas funcionalidades e uma interface interativa.

---

## ✨ Funcionalidades Principais

| Algoritmo | Complexidade Média | Destaques Didáticos |
| :--- | :--- | :--- |
| **Merge Sort** | `O(n log n)` | Divisão e conquista; estável e resiliente em todos os cenários. |
| **Insertion Sort** | `O(n²)` | `O(n)` no melhor caso. Excelente para dados pequenos ou quase ordenados. |
| **Bubble Sort** | `O(n²)` | Simples, mas ineficiente. Ótimo para visualizar o crescimento quadrático. |
| **Bogo Sort** | `O(n.n!)` | Embaralha até acertar. A piada perfeita para ensinar complexidade. |

O projeto gera gráficos comparativos que traçam:
-   📈 **Curvas Empíricas (Linhas Sólidas):** O tempo médio de execução medido na sua máquina.
-   📉 **Curvas Teóricas (Linhas Tracejadas):** As curvas da Notação Big O (`n log n`, `n²`, etc.), normalizadas para se alinharem com os dados e facilitarem a comparação visual.

---

## 🛠️ Estrutura e Formas de Uso

Este projeto pode ser utilizado de duas maneiras:

1.  **💻 Via Scripts de Linha de Comando (CLI):** Rápido, direto e ideal para testes específicos.
2.  **🔬 Via Jupyter Notebook (Recomendado para Aprendizado):** Interativo, visual e com explicações passo a passo.

```
SortingAlgorithms/
├─ README.md                       # Você está aqui!
├─ big_O_PyNorte.ipynb             # O notebook interativo completo.
├─ bogosort.py                     # Script CLI dedicado ao Bogo Sort.
└─ venv/                           # (Opcional) Ambiente virtual.
```

---

## ⚙️ Instalação e Configuração

**1. Clone o Repositório:**
```bash
git clone https://github.com/theunrealryan/SortingAlgorithms.git
cd SortingAlgorithms
```

**2. (Opcional mas recomendado) Crie um Ambiente Virtual:**
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

**3. Instale as Dependências:**
```bash
pip install numpy matplotlib pandas "ipywidgets>=7.0.0"
```

**4. (Apenas para Jupyter) Habilite os Widgets:**
Se você planeja usar o notebook interativo, habilite a extensão:
```bash
# Para Jupyter Notebook Clássico
jupyter nbextension enable --py widgetsnbextension

# Para JupyterLab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

---

## 🚀 Como Executar

### Modo 1: Jupyter Notebook Interativo

O notebook (`big_O_PyNorte.ipynb`) contém todas as análises, textos explicativos e um **Sandbox Interativo** para você configurar seus próprios experimentos com botões e sliders.

1.  Inicie o Jupyter:
    ```bash
    jupyter notebook
    ```
2.  Abra o arquivo `.ipynb`.
3.  Execute as células para seguir a análise guiada ou pule direto para o **Sandbox** no final.


### Modo 2: Script via Linha de Comando (CLI)

#### Analisando o `Bogo Sort`
Este benchmark dedicado é otimizado para não demorar uma eternidade:
```bash
python bogosort.py
```
Ele executa dois experimentos: um para mostrar a variação do tempo para `n=8`, e outro para plotar o crescimento explosivo de `n=2` a `n=8`.

---

## 🧪 Experimentos Sugeridos

| Insight a Obter | Como Configurar | O Que Observar |
| :--- | :--- | :--- |
| **Ponto de Cruzamento** | Compare `Insertion` vs `Merge` com `n` denso no início: `10, 20, 30... 150`. | `Insertion Sort` é mais rápido para `n` muito pequeno. Observe onde a linha do `Merge Sort` o ultrapassa. |
| **Melhor Caso do Insertion** | Compare `Insertion` e `Merge` no cenário `Ordenado`. | `Insertion Sort` se comporta como `O(n)` (uma linha reta), superando o `Merge Sort` de forma massiva. |
| **Resiliência do Merge** | Compare o `Merge Sort` nos cenários `Aleatório`, `Ordenado` e `Invertido`. | Seus tempos de execução serão quase idênticos, provando sua estabilidade `O(n log n)`. |
| **O Abismo Fatorial** | No script `bogosort.py`, altere o limite superior de `n` de 8 para 9. | Observe o tempo de execução saltar de segundos/minutos para... talvez horas? **Não recomendado!** |

---

## 📜 Licença

Este projeto é distribuído sob a **Licença MIT**. Sinta-se à vontade para usar, modificar e distribuir o código para fins educacionais ou de qualquer outra natureza. Consulte o arquivo [`LICENSE`](LICENSE) para mais detalhes.
