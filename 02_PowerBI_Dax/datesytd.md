### DATESYTD

> Sintaxe **DATESYTD**: `DATESYTD(dimCalendario[colunaData])`

Tabela de Amostra: (Vendas)
|Produto|Qtd Vendida|Loja|Data|Preco UN|Custo UN|Faturamento|Custo|Lucro|Marca|Categoria|
|-|-|-|-|-|-|-|-|-|-|-|
|Iphone 6S|2|Loja 2|01/01/2026|1900|1150|3800|2300|1500|Apple|Celular|
|Smart TV 50' 4K|5|Loja 1|01/01/2026|2000|1250|10000|6250|3750|Philco|Televisão|
|...|...|...|...|...|...|...|...|...|...|...|

Vamos calcular o faturamento total da tabela:
```
total_faturamento = SUM(Vendas[Faturamento])
```

Para calcularmos o faturamento acumulado do ano, usaremos **CALCULATE** com **DATESYTD**:
```
faturamento_ytd = 
CALCULATE(
    [total_faturamento],
    DATESYTD(dimCalendario[data])
)
```

> Quando vira o ano dez/2025 para jan/2026, o valor zera novamente!

### Como o DATESYTD funciona "Por Baixo dos Panos"?
O `DATESYTD` não é apenas um filtro mágico. Ele avalia a data mais recente que está visível no seu relatório (contexto de filtro atual) e retorna uma **tabela de uma única coluna** contendo todas as datas desde o dia 1º de janeiro daquele mesmo ano até a data avaliada. 

Por exemplo, se o seu gráfico está exibindo uma linha para **15 de Março de 2026**, o `DATESYTD` gera internamente uma lista de `01/01/2026` até `15/03/2026` e entrega para a `CALCULATE` filtrar a faturamento.

### 🎛️ Parâmetro Oculto: Ano Fiscal Diferente (O Pulo do Gato)
Pouca gente sabe, mas o `DATESYTD` aceita um **segundo argumento opcional** para empresas que não fecham o ano em 31 de Dezembro (comum em multinacionais ou órgãos públicos que usam ano fiscal).

Sintaxe Avançada:
```dax
faturamento_ytd_fiscal = 
CALCULATE(
    [total_faturamento],
    DATESYTD(dimCalendario[data], "06-30") -- O ano vai resetar no dia 30 de Junho!
)