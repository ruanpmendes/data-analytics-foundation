## Funções básicas do Excel

## Potenciação

> Para potenciação, utilizamos "^" para indicor a operação de potência. Ex: 2^2 = 4

## MULT

> =MULT(célula;célula) ou =MULT(célula:célula)

> OBS: Duplo Clique no canto inferior da célula, arrasta as fórmulas/formatação para todas as linhas.

## MAIOR e MENOR

Diferentemente de MAX e MIN, que pega somente o valor MÁXIMO ou MÍNIMO, com essas duas fórmulas, consegue pegar o 3° maior, o 5° maior, 2° menor, etc...

> =MAIOR/MENOR(matriz;posicao_rank)

ex:

>       3° maior: =MAIOR(H1:H9;3)
>
>       5° menor: =MENOR(H1:H9;5)

## Trancamento de Células (`F4`)

O trancamento serve para **fixar** referências de células ao arrastar ou copiar uma fórmula, evitando que o Excel/Google Sheets altere o endereço da célula de forma indesejada.

- **Trancamento Total (`$A$1`):** Trava a **coluna e a linha** simultaneamente; a referência não se move para lado nenhum ao arrastar a fórmula.
- **Trancamento Parcial de Linha (`A$1`):** Trava **apenas a linha**; ao arrastar para os lados a coluna muda, mas ao arrastar para baixo a linha permanece fixa.
- **Trancamento Parcial de Coluna (`$A1`):** Trava **apenas a coluna**; ao arrastar para baixo a linha muda, mas ao arrastar para os lados a coluna permanece fixa.

> **Atalho:** Pressione a tecla **`F4`** (ou `Fn + F4` em alguns notebooks) em cima da referência para alternar entre os tipos de trancamento.

## CONT.VALORES e CONT.NUM

CONT.VALORES conta células diferentes de vazio. CONT.NUM conta as células onde tem somente números.

## SUBTOTAL

Tira os filtros/ocultos da função esperada.

> ex: SUBTOTAL(9;matriz) --9 é o nro da função de soma. Matriz poderia ser B2:B19

## REMOÇÃO DE CÉLULAS VAZIAS

Selecionar todo os dados > F5 > Ir Para > Especial > Em Branco > Ctrl + - > Excluir Linha Inteira.

Esse processo irá selecionar todas as células vazias na matriz selecionada. E vai remover todas elas.

## Opção de Cálculo

Quando temos muitas fórmulas em uma planilha, e a planilha é grande, muita das vezes ao alterar algum campo que entre no cálculo de alguma fórmula, ela dá uma travada. Para resolver isso, devemos ir na aba `Fórmulas` e alterar em `Opções de Cálculo`, de `Automático` para `Manual`. Com isso, ao alterar algum campo, os cálculos só serão refeitos após dar F9 (ainda ficará Manual, mas realizará os ajustes já feitos) ou voltarmos para `Automático`, deixando assim, para atualizar tudo, uma única vez. Obetendo assim um melhor desempenho.

## Auditoria de Fórmulas (Aba Fórmulas)

Ferramentas essenciais para encontrar a causa raiz de erros, entender a dependência entre células e validar planilhas complexas antes de entregar relatórios gerenciais.

### 1. Rastrear Precedentes

- **O que faz:** Desenha setas azuis apontando para todas as células que **fornecem dados** para a fórmula da célula selecionada.
- **Uso prático:** Responder à pergunta: _"De onde vêm os valores que alimentam esta conta?"_.

### 2. Rastrear Dependentes

- **O que faz:** Desenha setas apontando para quais outras células da planilha **dependem do resultado** da célula selecionada.
- **Uso prático:** Responder à pergunta: _"Se eu alterar ou apagar esta célula, o que mais vai quebrar na planilha?"_.

### 3. Avaliar Fórmula

- **O que faz:** Abre uma janela passo a passo que executa a fórmula em partes, sublinhando e resolvendo uma operação por vez.
- **Uso prático:** Identificar exatamente em qual pedaço de uma fórmula extensa ou aninhada (ex: um `SE` com `AND` e `PROCX` juntos) o erro está acontecendo.

### Depuração (Debugging)

- **O que é:** O processo de investigar, isolar e corrigir falhas ou comportamentos inesperados em cálculos e modelos de dados.
- **Dica Pro de Depuração:**
  1. Use **Rastrear Precedentes** para ver o caminho dos dados.
  2. Use **Avaliar Fórmula** para ver o cálculo acontecendo quadro a quadro.
  3. Use **Remover Setas** para limpar a visualização da tela ao terminar.
