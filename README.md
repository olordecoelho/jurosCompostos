# Calculadora de juros compostos

Esta é uma calculadora de juros compostos que recebe como entrada o capital inicial, a taxa de juros e o tempo de investimento e retorna o saldo após o período.

## Variáveis

O código possui três variáveis:

- `capitalinicial`: armazena o valor do capital inicial informado pelo usuário.
- `juros`: armazena a taxa de juros informada pelo usuário.
- `tempo`: armazena o tempo de investimento informado pelo usuário.

## Entrada de dados

O código utiliza a função `input()` para receber a entrada de dados do usuário. O usuário é solicitado a informar o valor do capital inicial, a taxa de juros e o tempo de investimento. O código verifica se as entradas são válidas, ou seja, se o capital inicial e a taxa de juros são maiores ou iguais a 0 e se o tempo é maior ou igual a 0.

## Cálculo

O cálculo do saldo após o período é feito utilizando a fórmula de juros compostos:
Montante = Capital Inicial * (1 + Juros / 100) ** Tempo

![Untitled](https://www.notion.so/Calculadora-de-juros-compostos-37f566526d36455c9af20052bccc2e6f?pvs=4#0f4cec6ef3684308a151f6ce9cee3de6)

## Saída de dados

O código utiliza a função `print()` para exibir o saldo após o período. A saída é formatada utilizando a letra 'f' antes das aspas, permitindo a inclusão de variáveis no texto.

## Exemplo:

![Untitled](https://www.notion.so/Calculadora-de-juros-compostos-37f566526d36455c9af20052bccc2e6f?pvs=4#4be496e984ed493f840d61ce5858ab13)