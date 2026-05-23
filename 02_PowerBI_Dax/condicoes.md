### **IF**

> Sintaxe: `IF(Condicao,ValorSeVerdadeiro,ValorSeFalso)`

Amostra de Dados
|Produto|Tamanho Pedido|Data Venda|Dia da Semana|Preco Unitario|Cliente|Sexo|Nro Filhos|
|-|-|-|-|-|-|-|-|
|HL1005|2|11/06/2025|2|1500|Gabriel Assis|M|0|
|HL1006|1|12/06/2025|3|800|Thaís Mourda|F|0|

> Criar Coluna de Tipo do Ticket (Alto, Médio, Baixo, com base no valor)
```
Tipo do Ticket =
IF(
    TabelaVendas[Preco Unitario] >= 4000,
    "Ticket Alto",
    IF(
        TabelaVendas[Preco Unitario]>=2000,
        "Ticket Médio",
        "Ticket Baixo"
    )
)
```

---

### **AND ( && )**

> Sintaxe: `Condicao1 && Condicao2` -- Utiliza-se dois "&" para simbolizar o AND.

Dias das mães chegou, e temos que aplicar desconto de 20% no Preço Unitário para as mamães, para isso, devemos criar uma coluna. Onde se o cliente for do sexo `F` e ter 1 ou filho(a) ou mais, o Preço Unitário deve receber o desconto de 20%.

```
Preco Dia das Maes =
IF(
    TabelaVendas[Sexo] = "F" && TabelaVendas[Nro Filhos] > 0,
    TabelaVendas[Preco Unitario] * 0.8,
    TabelaVendas[Preco Unitario]
)
```

---

### **OR ( || )**

> Sintaxe: `Condicao1 || Condicao2` -- Utiliza-se dois "|" para simbolizar o OR.

O chefe pediu para analisar as vendas de dias da semana e dias do fim de semana. Para isso, iremos criar uma nova coluna, baseada na coluna `Dia da Semana` utilizando `OR`.

```
IF(
    TabelaVendas[Dia da Semana] = 1 || TabelaVendas[Dia da Semana] = 7,
    "Fim de Semana",
    "Dia Útil"
)
```
---

### **ISBLANK**
A Função `ISBLANK` simplesmente olha para o dado e responde com `True` ou `False`. 

- Isso está vazio? Retorna `True`
- Isso não está vazio? Retorna `False`

**Extamente** por isso, que `iSBLANK` é utilizado com o `IF`. 
> Sintaxe: `ISBLANK([Medida])`

#### **Cenário 1:**
Você montou uma Matriz mostrando a meta de captação dos assessores. O problema é que um assessor novato entrou ontem e ainda não tem dados de vendas. O Power BI vai deixar um buraco feio e vazio na frente do nome dele. Ai entra o ISBLANK para colocar um "R$ 0,00" ou um texto explicativo.

```
Comissao_Tratada = 
IF(
    ISBLANK([Total_Comissao]),
    0,
    [Total_Comissao]
)
```
> Agora em vez de deixar um espaço em branco na matriz, o assessor novo, aparece com "R$ 0,00".

#### **Cenário 2:**
Se montarmos uma medida que calcula o crescimento mês a mês, comparando o mês atual com o mês anterior. Se a empresa não vendeu nada no mês passado(é o 1° mês da base), a medida de mês anterior retorna `BLANK`. Tentar dividir algo por `BLANK` vai quebrar o gráfico/cartão.

```
crescimentoMoM =
IF(
    ISBLANK([faturamento_mes_anterior]),
    BLANK(),
    DIVIDE(
        [faturamento_atual] - [faturamento_mes_anterior],
        [faturamento_mes_anterior],
        0
    )
)
```
> Se o mês anterior for vazio, não será calculado o crescimento, retorna vazio para esconder a linha no gráfico.

#### **Cenário 3:**
O gestor pediu um ranking de todos os assessores da corretora, baseado no total vendido. A corretora tem 100 assessores, mas apenas 80 vnederam esse mês. Se fizer `RANKX` direto, o Power BI vai rankear os 80 primeiros normalmente. Porém os outros 20 que não venderam nada, vão apareceer todos empatados na 81° posição.

```
ranking_assessores =
IF(
    ISBLANK([total_comissao]),
    BLANK(),
    RANKX(
        ALL(dAssessor),
        [total_comissao]
    )
)
```

> Se o assessor não tiver vendas, ele não aparecerá no ranking. Deixando-o mais limpo.