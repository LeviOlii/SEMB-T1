# 🔍 Verificação de Conectividade em Grafos (DFS Iterativa)

Este projeto implementa um **algoritmo em C** para verificar se um grafo não direcionado é **conexo**. A entrada é uma **matriz de adjacência** armazenada em um arquivo `.txt`, e o programa realiza uma **busca em profundidade (DFS)** de forma **iterativa**, sem uso de recursividade ou alocação dinâmica.

---

## 🧠 Contexto do Projeto

Este código foi desenvolvido como parte do **Trabalho T1** da disciplina **Sistemas Embarcados**, ministrada pelo professor **Elias Teodoro da Silva Júnior** no **Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Fortaleza**.

O foco principal é explorar de forma simulada **as principais etapas no processo de desenvolvimento de aplicações embarcadas**. Na etapa atual, o objetivo consiste em escolher um algoritmo, implementá-lo em linguagem C e validar seu funcionamento.

---

## 👨‍💻 Autores

- **Levi Oliveira Bernardo**  
- **Luís Fernando Soares Sales**

---

## ⚙️ Funcionalidades da Implementação do Algoritmo

- Leitura de um **arquivo de texto** contendo a matriz de adjacência (`0` e `1`).
- Armazenamento em **estrutura estática** (`unsigned char`).
- Implementação de **DFS iterativa** com pilha estática.
- Exibição do resultado: **“O grafo é conexo”** ou **“O grafo não é conexo”**.

---

## 📂 Estrutura de Pastas

```bash
.
├── docs/
│   └── doxygen docs...          # Documentação em Doxygen da implementação em C
├── app/
│   ├── grafo_conexo.c           # Implementação principal
│   ├── grafo_conexo.exe         # Executável após compilação
│   └── validador_geral.py       # Programa de validação do algoritmo
├── include/
│   └── grafo_conexo.h           # Cabeçalho da implementação do algoritmo C com protótipos e definições
├── validation_data/
│   ├── grafo_p0.01_1.txt        # Exemplos de grafos com diferentes probabilidades para validação
│   ├── grafo_p0.01_2.txt      
│   ├── ...
│   ├── grafo_p0.25_1.txt        # Exemplos de grafos com diferentes probabilidades para validação
│   ├── grafo_p0.25_2.txt      
│   └── ...
├── images/
│   ├── acuracia_comparacao.png  # Gráfico de acurácia C x Python
│   ├── grafo_conexo_3d.gif      # Animação 3D do grafo conexo
│   └── grafo_nao_conexo_3d.gif  # Animação 3D do grafo não conexo
├── Doxyfile                     # Arquivo de configuração do Doxygen
└── README.md     

```

## 🧩 Formato da Entrada (`.txt`)

O arquivo deve conter uma **matriz quadrada** de `0` e `1`, representando as **ligações (arestas)** entre os vértices do grafo.  
Cada linha corresponde a um vértice e cada coluna indica se existe (1) ou não (0) uma conexão entre eles.

Exemplo de grafo simples com **4 vértices**:

```txt
0 1 0 1
1 0 1 1
0 1 0 0
1 1 0 0

```

💡 Dica:
O valor grafo[i][j] = 1 indica que existe uma aresta entre os vértices i e j.

O valor grafo[i][j] = 0 indica ausência de ligação.

A diagonal principal deve conter apenas zeros (grafo[i][i] = 0), já que um vértice não é conectado a si mesmo.

---

## 🚀 Como Compilar e Executar

Antes de tudo, vá no diretório ./app

### 1️⃣ Compilação

```bash
gcc ./grafo_conexo.c -o grafo_conexo
```

### 2️⃣ Execução
```bash
./grafo_conexo ../validation_data/'nome_do_arquivo.txt'
```

---

## 🧪 Exemplo de Saída

```bash
Matriz de adjacência (89 x 89) carregada com sucesso.

Resultado: O grafo é CONEXO.
```

ou

```bash
Matriz de adjacência (89 x 89) carregada com sucesso.

Resultado: O grafo NÃO é conexo.
```

---

## 📊 Script de Validação e Análise (validador_geral.py)

O validador_geral.py foi com o objetivo de validar automaticamente o algoritmo em C comparando seus resultados com os obtidos por uma biblioteca de referência do Python (NetworkX).

### ⚙️ Funcionamento

O script executa uma bateria de testes automatizada, gerando diversos grafos aleatórios com diferentes probabilidades de conexão entre os vértices. Ele compara a saída do algoritmo em C com a função nx.is_connected() (do NetworkX, considerada confiável), mede a acurácia dos resultados, mostra a comparação entre a saída de cada teste no terminal e gera um gráfico da acurácia por probabilidade de teste.

1. Geração dos grafos:

* Cria arquivos .txt representando matrizes de adjacência de grafos aleatórios.
* Cada arquivo é salvo na pasta validation_data/.
* Caso os arquivos já existam, o script não os recria (mantendo consistência nos testes).

2. Execução automática do código em C:

* O script chama o executável (grafo_conexo.exe) para testar cada arquivo de grafo.
* Usa o módulo subprocess para capturar a saída do terminal.
* Comparação de resultados:
* Verifica se o resultado do programa em C coincide com o resultado do NetworkX.

3. Análise e visualização:

* Calcula a acurácia média para cada probabilidade de aresta.
* Gera um gráfico de acurácia (%) em função da probabilidade, mostrando o desempenho do algoritmo.

### 🧮 Exemplo de Saída no Terminal

```bash
p=0.05 | ./validation_data/grafo_p0.05_1.txt | esperado=True | obtido=True
>> Probabilidade 0.05 → Acurácia: 100.0%
```

### 📈 Exemplo de Gráfico Gerado

O gráfico mostra a acurácia do algoritmo em C em relação à implementação Python (is_connected()):

```css
Acurácia (%)
│
│           ● ● ● ● ● ● ● ●
│          /
│         /
│────────/───────────────────────────────► Probabilidade de Aresta (p)
     0.01   0.05   0.10   0.15   0.25

```
*💡 A validação automática comprovou 100% de correspondência entre os resultados do algoritmo em C e o Python em todos os casos testados.*

## 🧾 Licença
Uso acadêmico livre, desde que citados os autores originais.
📚 Desenvolvido com fins educacionais para o IFCE - Campus Fortaleza.

---

## 🧩 Geração Automática de Documentação (Doxygen)
O código contém comentários padronizados em Doxygen. 
Para acessar a documentação, basta ir na pasta docs e acessar o index.html

---
