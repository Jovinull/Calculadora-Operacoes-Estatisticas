# Calculadora de Operações Estatísticas

## Descrição

Este projeto é uma tarefa da primeiro mês da apostila de IA da Dra. Stephanie Kamarry. O objetivo é desenvolver uma aplicação em Python que realiza operações estatísticas básicas, como média, mediana e desvio padrão, sem utilizar bibliotecas externas, com exceção da função matemática `sqrt`.

## Funcionalidade

A aplicação coleta uma lista de números fornecida pelo usuário e calcula as seguintes operações estatísticas:

1. **Média (Média Aritmética)**:
   - A média é a soma de todos os elementos dividida pelo número total de elementos.
   - Fórmula abaixo, onde N é o número de elementos: 

![Fórmula da Média](https://i.imgur.com/mFBoijP.jpg)

2. **Mediana**:
   - A mediana é o valor central de uma lista de números ordenada.
   - Se o número de elementos for ímpar, a mediana é o valor do meio.
   - Se o número de elementos for par, a mediana é a média dos dois valores centrais.

3. **Desvio Padrão**:
   - O desvio padrão é uma medida da dispersão dos valores em relação à média.
   - Calcula-se a média dos números, depois a soma das diferenças quadradas de cada número em relação à média, divide-se pela quantidade de números e, finalmente, extrai-se a raiz quadrada dessa média.
   - Fórmula abaixo, onde x representa cada número e N é o número de elementos:

![Fórmula do Desvio Padrão](https://i.imgur.com/rcfp6vk.png)

## Como o Projeto Foi Feito

1. **Coleta de Dados**:
   - O usuário é solicitado a inserir uma lista de números separados por espaços.
   - A entrada é processada e convertida em uma lista de números.

2. **Cálculo da Média**:
   - A soma dos números é calculada.
   - O número total de elementos é contado.
   - A soma é dividida pelo número de elementos para obter a média.

3. **Cálculo da Mediana**:
   - Os números são ordenados em ordem crescente.
   - Verifica-se se o número de elementos é par ou ímpar.
   - A mediana é determinada com base na posição central dos números ordenados.

4. **Cálculo do Desvio Padrão**:
   - A média dos números é calculada.
   - Calcula-se a soma das diferenças quadradas entre cada número e a média.
   - A variância é obtida dividindo-se a soma das diferenças quadradas pelo número de elementos.
   - A raiz quadrada da variância é calculada para obter o desvio padrão.

## Testes Unitários

O projeto possui testes unitários destinados a assegurar a precisão dos cálculos realizados pelas funções de cálculo estatístico. Esses testes são desenvolvidos utilizando o módulo `unittest` do Python. Neles foram incluidos entradas padrão com respostas previamente verificadas, garantindo assim resultados corretos.

Os testes unitários são importantes porque garantem que cada parte do código funciona como esperado, ajudando a identificar problemas e falhas rapidamente durante o desenvolvimento.

Os seguintes testes estão incluídos no projeto:

- **Teste de Cálculo da Média**: Verifica se a função `calcular_media` retorna a média correta para uma lista de números.
- **Teste de Cálculo da Mediana**: Confirma se a função `calcular_mediana` retorna a mediana correta, tanto para listas com número ímpar quanto par de elementos.
- **Teste de Cálculo do Desvio Padrão**: Garante que a função `calcular_desvio_padrao` calcule o desvio padrão de forma precisa.
- **Teste de Cálculo da Moda**: Verifica se a função `calcular_moda` retorna a moda correta para uma lista de números.

**OBS:** Para executar os testes, você pode deve utilizar o comando `python -m unittest -v` no terminal.

## Link para a Apostila

Consulte a apostila fornecida pela Professora Kamarry através do [link](https://docs.google.com/document/d/1E15j1WMReA4unM3atGOMGEvwEaN5kylx22nWoz2DffQ/edit#heading=h.4r9g73p14p37).

## Referências

### **Cálculos:**
  - [Desvio padrão](https://pt.wikipedia.org/wiki/Desvio_padr%C3%A3o). Acessado em: 16/05/2024.
  - [Mediana (estatística)](https://pt.wikipedia.org/wiki/Mediana_(estat%C3%ADstica)). Acessado em: 16/05/2024.
  - [Média](https://pt.wikipedia.org/wiki/M%C3%A9dia). Acessado em: 16/05/2024.

### **Python:**
  - [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html). Acessado em: 16/05/2024.
