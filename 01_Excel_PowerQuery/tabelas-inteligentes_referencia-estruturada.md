### **Tabelas Inteligentes e Referência Estruturada**

> F4 trava a célula com ($a$1)

```
@           - Referência de linha
[]          - Referência de nome_coluna
#All        - Referência da tabela inteira
#Headers    - Referência os Headers
```

**Problema**:

Se os dados forem um intervalo normal, para calcular o faturamento por exemplo, temos que fazer: `b2\*c2` e arrastar até o fim da coluna.
Se o sistema gerar mais 50 vendas amanha, as formulas não vão acompanhar automaticamente. Teremos que arrastar tudo de novo.

**Solução**:

Usando **_Tabelas Inteligentes_**, o Excel enxerga a tabela como um Banco de Dados. Se adicionar uma lnha nova, ela herda todas as fórmulas automaticamente.
Se criar uma fórmula na primeira linha, ela se expande sozinha para a colua inteira (Coluna Calculada)

**Como criar**:

Selecione um celula do intervalo, e dê `Ctrl` + `Alt` + `T`.
Assim que virar uma tabela, as linhas e colunas da tabela ganharam cores diferentes. Filtros automáticos e uma nova aba surge, permitindo por exemplo mudar o nome da tabela.

> Obs: Mudar sempre o nome para algo que faça sentido.

### **Referências Estruturadas**

Em um intervalo normal, para somar coluna de vendas por exemplo, usaria:
`=SOMA(D2:D100)`. Se alguem olhar ou eu mesmo futuramente, não saberia o que tem em D logo de cara.
Na tabela Inteligente usamos Referência Estruturada. O Excel para de olhar para o endereço da célula(D2) e passa a olhar para o nome da coluna.
Por exemplo, se o nome da coluna for 'Valor Venda', para criar a mesma coluna somando as vedas, seria: `=SOMA([Valor Venda])`

**Exemplo de fórmulas na Tabela Inteligente:**

Amostra de Dados - Tabela DadosVendas
|Região | Qtd | Preço
|-|-|-|
|Norte | 2 | 21.50
|Sul | 3 | 19.5
|...|...|...|
...

**_Somando linhas (calculando valor total da venda)_**

```
= [@Qtd] \* [@Preço] # O @ avisa: "Multiplique a Qtd desta linha pelo Preço desta linha"
```

**_Somando colunas (Agregação: Achando a quantidade total vendida)`_**

```
= SOMA(DadosVendas[Qtd]) # Você aponta para o Nome da Tabela + [nome_coluna]. Se adicionar 1K linhas amanhã, essa fórmula continua funcionando perfeitamente.
```

**_Como somar com filtros (função SUBTOTAL)_**

Como exemplo da formula acima, somamos a quantidade total vendida, mas se aplicarmos um filtro na tabela, esse número não irá mudar, a função `SOMA` ignora os filtros e continua somando linhas ocultas. Se for querer uma soma que respeita os filtros, o ideal é usar `SUBTOTAL`!

```
Sintaxe: =SUBTOTAL(nro_funcao; intervalo/coluna)
```

O nro_funcao da `SOMA` é o `9`. Então para somar dinamicamente a quantide vendida:

```
=SUBTOTAL(9; DadosVendas[Qtd])
```

**_Soma acumulada (linha a linha) filtrando Região (similar a um `WHERE` em BD)_**

Para fazer uma acumulada de uma tabela Inteligente, fazemos um "truque" com o travamento por célula ($) para fixar o ponto de partida (topo da tabela) até a linha atual.

```
=SOMA($B$2:[@Faturamento]) # Isso está dizendo ao Excel: "Soma desde o primeiro Dado da coluna Faturamento até a linha onde estou agora"
```

**_Misturando isso com o filtro para a Região "Norte", utilizaremos a função `SOMASES`._**

```
Sintaxe: =SOMASES(coluna_que_será_somada; coluna_do_critério; critério)
```

ficaria assim:

```
=SOMASES($B$2:[@Faturamento];$A$2:[@Região];"Norte")

O que essa fórmula está fazendo: "Excel, use a função SOMASES. Olhe para a coluna Faturamento desde o início até a linha atual. Mas só some se, na coluna Região (desde o início até a linha atual), o valor for igual a "Norte"."
```

**_Soma acumulada agrupando por Região (similar a um `GROUP BY` em BD)_**

```
=SOMASES($B$2:[@Valor Venda];$A$2:[@Região];[@Região])
O que essa fórmula está fazendo:

1. $B$2:[@Valor Venda] -> "Excel, seu limite de soma começa na primeira linha de dados fixa ($B$2) da coluna Valor Venda e vai expandindo até a linha atual"

2. $A$2:[@Região] -> "Para aplicar o filtro, olhe a coluna Região desde o topo fixo ($A$2) até a linha atual."

3. [@Região] -> "Aqui está o segredo do GROUP BY! O critério de filtro é o valor da Região desta linha atual."
```

> ANOTAÇÃO IMPORTANTE: Usamos o travamento por célula (ex: $B$2 e $A$2) no início do intervalo para dizer ao Excel:
>
> "Comece o meu intervalo de soma estritamente na célula física da primeira linha de dados, travando-a, e estenda esse intervalo de forma dinâmica até a linha atual usando a Referência Estruturada."

> Travamento com $ == Garante estabilidade, evita o bug de auto-correção do Excel e força o início do intervalo na primeira linha de dados, ignorando o Header.

> - F4 travaa a célula ###

---

### **_Exercício:_**

#### 1. Crie uma terceira coluna nessa tabela e dê o nome de [Acumulado Depto]. Sua missão: Escreva a fórmula de soma acumulada com o efeito `GROUP BY` (janela de partição) utilizando as Referências Estruturadas que acabamos de aprender. Essa fórmula deve calcular o orçamento acumulado específico de cada departamento à medida que as linhas descem.

```
=SOMASES($B$2:[@Salário];$A$2:[@Departamento];[@Departamento])
```

#### 2. Seu gestor quer analisar as vendas na tela e quer que você monte um somatório da coluna de faturamento na célula G2. Mas atenção: ele quer filtrar a tabela por Category (Categoria) e ver o valor de G2 mudar dinamicamente na tela, somando apenas o que estiver visível.

Na célula G2, monte a fórmula correta usando o `SUBTOTAL` e Referências Estruturadas para somar a coluna [Revenue].

Amostra dos Dados
|Product |Category |Revenue
|-|-|-|
|Smartphone |Eletrônicos |4500
|Sofá 3 Lugares |Móveis |2800
|Notebook Pro |Eletrônicos |8500
|Mesa de Jantar |Móveis |1900
|Fone Bluetooth |Eletrônicos |600

```
=SUBTOTAL(9, Sales[Revenue])
```

#### 3. Para controlar o orçamento anual de contratações, a diretoria quer ver o custo acumulado de salários subindo linha a linha.

Crie uma terceira coluna na tabela chamada [Running_Total]. Na primeira linha dessa coluna, use a fórmula inquebrável que aprendemos usando a função SUM para fazer o acumulado da coluna [Salary].

| Employee     | Salary |
| ------------ | ------ |
| Ana Silva    | 4000   |
| Bruno Costa  | 5500   |
| Carlos Souza | 3800   |
| Daniela Lima | 7000   |

```
=SUM($B$31:[@Salary])
```
