# Questão 1
# Sistema de Ordenação Flexível usando o Design Pattern Strategy

Este projeto implementa um sistema capaz de ordenar dados usando diferentes algoritmos de ordenação. O sistema permite trocar o algoritmo de ordenação em tempo de execução, utilizando o design pattern Strategy.

## Algoritmos de Ordenação Implementados

O projeto inclui a implementação de três algoritmos de ordenação diferentes:

1. Bubble Sort: realiza ordenação por meio de comparações adjacentes e trocas de elementos.
2. Selection Sort: seleciona repetidamente o menor elemento restante e o coloca na posição correta.
3. Merge Sort: divide a lista em sub-listas menores, as ordena recursivamente e, em seguida, as mescla para obter a lista final ordenada.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

- `SortStrategy`: Contém a definição da classe abstrata `SortStrategy`, que é a base para os diferentes algoritmos de ordenação.
- `BubbleSortStrategy`: Implementação do algoritmo Bubble Sort, que herda de `SortStrategy`.
- `SelectionSortStrategy`: Implementação do algoritmo Selection Sort, que herda de `SortStrategy`.
- `MergeSortStrategy`: Implementação do algoritmo Merge Sort, que herda de `SortStrategy`.
- `Sorter`: Implementação da classe `Sorter`, que utiliza a estratégia de ordenação selecionada.

## Como Usar

1. Clone o repositório para o seu ambiente local.
2. Execute o arquivo `questao2.py` para ver o exemplo de uso do sistema de ordenação.

Certifique-se de ter o Python instalado em sua máquina.


# Questão 2
# Contador de Palavras

Este é um programa em Python que recebe uma frase, quebra em palavras e conta as palavras de acordo com critérios específicos.

## Funcionalidades

O programa possui as seguintes funcionalidades:

- Contar todas as palavras da frase.
- Contar palavras com quantidades pares de caracteres.
- Contar palavras começadas com maiúsculas.

## Utilização

1. Execute o programa em Python.
2. Será solicitado que você digite uma frase.
3. Digite a frase desejada e pressione Enter.
4. O programa exibirá o total de palavras, palavras com quantidade par de caracteres e palavras começadas com maiúsculas.

## Exemplo

Digite uma frase: Olá, mundo! Este é um exemplo de frase.
Total de palavras: 7
Palavras com quantidade par de caracteres: 3
Palavras começadas com maiúsculas: 2


Neste exemplo, a frase "Olá, mundo! Este é um exemplo de frase." foi digitada. O programa contou 7 palavras, sendo 3 palavras com quantidade par de caracteres e 2 palavras começadas com maiúsculas.

## Padrão Observer

O padrão Observer foi utilizado para separar as responsabilidades do contador de palavras e dos observadores. A classe `WordCounter` é responsável por gerenciar os observadores e notificar as atualizações nos dados. A classe `WordCountObserver` é uma classe observadora que conta as palavras de acordo com os critérios definidos.


## Autor

Este projeto foi feito por Leonardo Mendonça Franco
