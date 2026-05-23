### **IF**

> Sintaxe: `IF(Condicao;ValorSeVerdadeiro;ValorSeFalso)`

Amostra de Dados
|Produto|Tamanho Pedido|Data Venda|Dia da Semana|Preco Unitario|Cliente|Sexo|Nro Filhos|
|-|-|-|-|-|-|-|-|
|HL1005|2|11/06/2025|2|1500|Gabriel Assis|M|0|
|HL1006|1|12/06/2025|3|800|Thaís Mourda|F|0|

> Criar Coluna de Tipo do Ticket (Alto, Médio, Baixo, com base no valor)
```
Tipo do Ticket =
IF(
    TabelaVendas[Preco Unitario] >= 4000;
    "Ticket Alto";
    IF(
        TabelaVendas[Preco Unitario]>=2000;
        "Ticket Médio";
        "Ticket Baixo"
    )
)
```

### **AND ( && )**

> Sintaxe: `Condicao1 && Condicao2` -- Utiliza-se dois "&" para simbolizar o AND.

Dias das mães chegou, e temos que aplicar desconto de 20% no Preço Unitário para as mamães, para isso, devemos criar uma coluna. Onde se o cliente for do sexo `F` e ter 1 ou filho(a) ou mais, o Preço Unitário deve receber o desconto de 20%.

```
Preco Dia das Maes =
IF(
    TabelaVendas[Sexo] = "F" && TabelaVendas[Nro Filhos] > 0;
    TabelaVendas[Preco Unitario] * 0.8;
    TabelaVendas[Preco Unitario]
)
```

### **OR ( || )

> Sintaxe: `Condicao1 || Condicao2` -- Utiliza-se dois "|" para simbolizar o OR.

O chefe pediu para analisar as vendas de dias da semana e dias do fim de semana. Para isso, iremos criar uma nova coluna, baseada na coluna `Dia da Semana` utilizando `OR`.

```
IF(
    TabelaVendas[Dia da Semana] = 1 || TabelaVendas[Dia da Semana] = 7;
    "Fim de Semana";
    "Dia Útil"
)
```