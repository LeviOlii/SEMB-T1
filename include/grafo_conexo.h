/**
 * -----------------------------------------------------------------------------
 *  @file grafo_conexo.h
 *  @brief Cabeçalho para o algoritmo de verificação de conectividade de grafos.
 *
 *  @details
 *      Este arquivo contém as definições, variáveis globais e protótipos das
 *      funções utilizadas na implementação do algoritmo de busca em profundidade
 *      (DFS) iterativa. O objetivo é verificar se um grafo não direcionado é conexo.
 *
 *  @authors
 *      - Luís Fernando Soares Sales
 *      - Levi Oliveira Bernardo
 *
 *  @date 22/10/2025
 *  @version 1.0
 *
 *  @note Desenvolvido como parte do Trabalho T1 da disciplina de Sistemas Embarcados,
 *        ministrada pelo professor Elias Teodoro Silva Júnior no IFCE - Campus Fortaleza.
 *
 * -----------------------------------------------------------------------------
 */

#ifndef GRAFO_CONEXO_H
#define GRAFO_CONEXO_H

#include <stdio.h>
#include <stdlib.h>

#define VERTICES 89 /**< Número máximo de vértices do grafo */

// -----------------------------------------------------------------------------
// Declaração das variáveis globais (definidas em grafo_conexo.c)
// -----------------------------------------------------------------------------
extern unsigned char grafo[VERTICES][VERTICES]; /**< Matriz de adjacência */
extern unsigned char visitado[VERTICES];        /**< Vetor de vértices visitados */
extern unsigned char pilha[VERTICES];           /**< Estrutura auxiliar de pilha */

// -----------------------------------------------------------------------------
// Protótipos de funções
// -----------------------------------------------------------------------------

// -----------------------------------------------------------------------------
// Função: carregarGrafo
// -----------------------------------------------------------------------------
/**
 * @brief Lê a matriz de adjacência a partir de um arquivo de texto.
 *
 * @param caminhoArquivo Caminho relativo ou absoluto do arquivo a ser lido.
 * @return int Retorna o número de vértices (N) lidos com sucesso,
 *         ou -1 se houver erro de leitura.
 *
 * @details
 *      A função realiza duas leituras:
 *          (1) Determina o número de colunas (N) lendo a primeira linha.
 *          (2) Reabre o arquivo e lê toda a matriz N x N de valores binários.
 */
int carregarGrafo(const char *caminhoArquivo);

// -----------------------------------------------------------------------------
// Função: verificarConectividade
// -----------------------------------------------------------------------------
/**
 * @brief Verifica se o grafo é conexo utilizando busca em profundidade (DFS) iterativa.
 *
 * @param n Número de vértices (tamanho da matriz de adjacência).
 * @return int Retorna 1 se o grafo for conexo, 0 caso contrário.
 *
 * @details
 *      A função utiliza uma pilha estática para explorar vértices conectados,
 *      evitando o uso de recursão. Cada vértice visitado é marcado no vetor global
 *      'visitado'. Ao final, se todos os vértices forem visitados, o grafo é conexo.
 */
int verificarConectividade(int n);

#endif // GRAFO_CONEXO_H
