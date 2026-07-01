### DATESBETWEEN

`DATESBETWEEN` é uma função de tabela. O objetivo dela é olhar para a tabelaCalendario e extrair uma tabela com uma única coluna, contendo uma lista de datas consecutivas, delimitada por um dia de início e um dia de fim, passados como parâmetros na função.

> Sintaxe: `DATESBETWEEN(tabelaCalendario[colunaData], dataInicio, dataFim)`

#### **Exemplos na prática**

#### Cenário 1: Campanha de Marketing

Imagine que uma Loja fez uma campanha de panfletagem e tráfego pago para o _Festival de Inverno_. A campanha não começou no 1° dia do mês e nem terminou no último. A campanha foi realizada de 12/05/2026 a 27/05/2026. O diretor quer ver o faturamento gerado apenas nesse período.

```
faturamento_festival_inverno =
CALCULATE(
    [total_faturamento], -- já fizemos a medida anteriormente.
    DATESBETWEEN(
        tabelaCalendario[data], -- Utilizar sempre tabelaCalendario
        DATE(2026, 5, 12), -- Ínicio da campanha
        DATE(2026, 5, 27)  -- Fim da campanha
    )
)
```

#### Cenário 2: Janela móvel dinâmica

O Dashboard precisa mostrar um card com faturamento dos últimos 30 dias com base na última data que temos vendas na tabela/banco. Para fazer isso, vamos utilizar `DATESBETWEEN` com `MAX`(último dia com dados).

```
faturamento_ultimos_30_dias =
-- 1. Descobre qual é o último dia com venda.
VAR UltimoDiaComVenda = MAX(fVendas[data_pedido])

-- 2. Calcula qual foi o dia 30 dias atrás.
VAR TrintaDiasAtras = UltimoDiaComVenda - 30

RETURN
CALCULATE(
    [total_faturamento],
    DATESBETWEEN(
        tabelaCalendario[data],
        TrintaDiasAtras,
        UltimoDiaComVenda
    )
)
```

#### **Comportamento com `BLANK()`**

O DAX é inteligente. Se não soubermos a data exata do início ou de fim, podemos passar a função `BLANK()` no lugar da data.

- `BLANK()` como dataInicio, o Power BI vai filtrar desde a primeira data existente na tabelaCalendário até o fim.
- `BLANK()` como dataFim, o Power BI vai filtrar da dataInicio passado até a última data existente na tabelaCalenário.
