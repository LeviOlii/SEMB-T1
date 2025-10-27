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

## ⚙️ Funcionalidades

- Leitura de um **arquivo de texto** contendo a matriz de adjacência (`0` e `1`).
- Armazenamento em **estrutura estática** (`unsigned char`).
- Implementação de **DFS iterativa** com pilha estática.
- Exibição do resultado: **“O grafo é conexo”** ou **“O grafo não é conexo”**.

---

## 📂 Estrutura de Pastas

```bash
.
├── docs/
│   └── doxygen docs...          # Implementação principal
├── src/
│   └── grafo_conexo.c           # Implementação principal
├── include/
│   └── grafo_conexo.h           # Cabeçalho com protótipos e definições
├── input/
│   ├── grafo_conexo_1.txt       # Exemplo de grafo conexo
│   ├── grafo_nao_conexo_5.txt   # Exemplo de grafo não conexo
│   └── ...
├── Doxyfile                     # Arquivo de configuração do Doxygen
└── README.md                    # Este arquivo

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

Antes de tudo, vá no diretório ./src

### 1️⃣ Compilação

```bash
gcc ./src/grafo_conexo.c -o grafo_conexo
```

### 2️⃣ Execução
```bash
./grafo_conexo
```

O código usa caminho relativo por padrão:

```c
const char *arquivoEntrada = "../input/grafo_conexo_1.txt";
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

## 🧾 Licença
Uso acadêmico livre, desde que citados os autores originais.
📚 Desenvolvido com fins educacionais para o IFCE - Campus Fortaleza.

---

## 🧩 Geração Automática de Documentação (Doxygen)
O código contém comentários padronizados em Doxygen. 
Para acessar a documentação, basta ir na pasta docs e acessar o index.html

---
