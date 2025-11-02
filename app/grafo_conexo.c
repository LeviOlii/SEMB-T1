/**
 * -----------------------------------------------------------------------------
 *  @file grafo_conexo.c
 *  @brief Implementação do algoritmo de verificação de conectividade em grafos.
 *
 *  @details
 *      O programa lê uma matriz de adjacência de um arquivo de texto (contendo 0 e 1),
 *      armazena os dados em uma estrutura estática e executa o algoritmo de
 *      busca em profundidade (DFS) de forma iterativa, sem uso de recursividade
 *      nem alocação dinâmica. O resultado indica se o grafo é ou não conexo.
 *
 *  @authors
 *      - Luís Fernando Soares Sales
 *      - Levi Oliveira Bernardo
 *
 *  @date 03/11/2025
 *  @version 1.0
 *
 *  @par License:
 *  Uso acadêmico livre com citação dos autores.
 *
 *  @par Instructions:
 *       - Na pasta raiz do projeto haverá uma pasta 'app/validation_data' contendo arquivos
 *         de exemplo com matrizes de adjacência (0s e 1s) que representam grafos gerados
 *         com diferentes probabilidades de haver conexão entre par de vértices.
 *         Estes arquivos podem ser usados para testar o programa.
 *         OBS: O caminho definido deve ser relativo à pasta onde fica o executável.
 *       - Na pasta app, compile o código com:  gcc ./grafo_conexo.c -o grafo_conexo
 *       - Execute o programa:   ./grafo_conexo "caminho_do_arquivo.txt"
 *       .
 */

#include "../include/grafo_conexo.h"

// -----------------------------------------------------------------------------
// Estruturas globais estáticas
// -----------------------------------------------------------------------------
unsigned char grafo[VERTICES][VERTICES]; /**< Matriz de adjacência do grafo */
unsigned char visitado[VERTICES];        /**< Vetor de controle de vértices visitados */
unsigned char pilha[VERTICES];           /**< Pilha auxiliar para DFS iterativa */

// -----------------------------------------------------------------------------
// Função: carregarGrafo
// -----------------------------------------------------------------------------

int carregarGrafo(const char *caminhoArquivo)
{
    FILE *arquivo;
    int i, j;
    int N = 0;
    int colunas_lidas = 0;
    int proximo_char;

    printf("Iniciando leitura da matriz de adjacência do arquivo '%s'...\n", caminhoArquivo);

    arquivo = fopen(caminhoArquivo, "r");
    if (arquivo == NULL)
    {
        printf("ERRO: O arquivo '%s' não foi encontrado.\n", caminhoArquivo);
        return -1;
    }

    // --- Determinar o número de colunas (N) pela primeira linha ---
    while (fscanf(arquivo, "%hhu", &grafo[0][colunas_lidas]) == 1)
    {
        colunas_lidas++;

        proximo_char = fgetc(arquivo);
        if (proximo_char == '\n' || proximo_char == EOF)
            break;
        else
            ungetc(proximo_char, arquivo);

        if (colunas_lidas >= VERTICES)
        {
            printf("ERRO: A primeira linha excede o limite de %d colunas.\n", VERTICES);
            fclose(arquivo);
            return -1;
        }
    }

    if (colunas_lidas == 0)
    {
        printf("ERRO: Arquivo vazio ou formato inválido (nenhum número encontrado).\n");
        fclose(arquivo);
        return -1;
    }

    N = colunas_lidas;
    fclose(arquivo);

    // --- Reabrir o arquivo e ler a matriz completa ---
    arquivo = fopen(caminhoArquivo, "r");
    if (arquivo == NULL)
        return -1;

    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            if (fscanf(arquivo, "%hhu", &grafo[i][j]) != 1)
            {
                printf("ERRO: Falha ao ler valor na posição [%d][%d]. Esperado %d x %d.\n", i, j, N, N);
                fclose(arquivo);
                return -1;
            }
        }
    }

    fclose(arquivo);
    printf("Matriz de adjacencia (%d x %d) carregada com sucesso.\n\n", N, N);
    return N;
}

// -----------------------------------------------------------------------------
// Função: verificarConectividade
// -----------------------------------------------------------------------------
int verificarConectividade(int n)
{
    int topo = -1;          // Inicialização do índice que representa o topo da pilha
    int atual = 0;          // Vértice inicial para a DFS e vértice atual em exploração
    int i;                  // Índice de iteração

    // Prepara vetor de visitados setando todas as posições como 0 (não visitado)
    for (i = 0; i < n; i++)
        visitado[i] = 0;

    // Inicia a DFS a partir do vértice 0
    pilha[++topo] = atual;      // Empilha o vértice inicial
    visitado[atual] = 1;        // Marca como visitado

    while (topo >= 0)
    {
        atual = pilha[topo--];

        // Percorre todos os vértices adjacentes ao atual
        for (i = 0; i < n; i++)
        {
            if (grafo[atual][i] == 1 && !visitado[i])
            {
                visitado[i] = 1;
                pilha[++topo] = i;
            }
        }

    }

    // Verifica se todos foram visitados
    for (i = 0; i < n; i++)
        if (!visitado[i])
            return 0;

    return 1;
}

// -----------------------------------------------------------------------------
// Função principal
// -----------------------------------------------------------------------------
/**
 * @brief Função principal de execução do programa.
 *
 * @return int Retorna 0 em caso de sucesso, 1 em caso de erro.
 *
 * @details
 *      Define o caminho relativo do arquivo de entrada, carrega a matriz de adjacência,
 *      executa o algoritmo de verificação de conectividade e exibe o resultado. 
 *      Permite passar o arquivo de entrada (.txt) como argumento na linha de comando.
 */
int main(int argc, char *argv[])
{
    int tam_grafo, conexo;
    const char *arquivoEntrada;

    // Verifica se o usuário passou o nome do arquivo na linha de comando
    if (argc < 2)
    {
        printf("Uso: %s <arquivo_entrada.txt>\n", argv[0]);
        return 1;
    }

    // Pega o nome do arquivo do argumento
    arquivoEntrada = argv[1];

    // Leitura e verificação
    tam_grafo = carregarGrafo(arquivoEntrada);
    if (tam_grafo <= 0)
        return 1;

    conexo = verificarConectividade(tam_grafo);

    // Exibe o resultado no terminal
    if (conexo)
        printf("Resultado: O grafo eh CONEXO.\n");
    else
        printf("Resultado: O grafo NAO eh conexo.\n");

    return 0;
}
