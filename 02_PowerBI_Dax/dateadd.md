### DATEADD

Permite fazer comparativos entre períodos.
Ex: Comparar o faturamento de Abril com o de Março, ou de Abril/2026 com Abril/2025.

> Sintaxe **DATEADD**: `DATEADD(tabelaData[colunaData], InvervaloParaDeslocar, Intervalo)`
>
> Sempre utilizar Data da tabela Calendário. (dimCalendario)

```
-- Para acharmos o faturamento do mês anterior:
faturamento_mes_anterior =
CALCULATE(
    [faturamento_total],
    DATEADD(
        dCalendario[data],
        -1,
        MONTH -- Poder ser "YEAR", "QUARTER", "DAY", etc
    )
)
```

```
-- Calculando percentual de crescimento Month Over Month:
%_crescimento_MoM =
DIVIDE(
    [faturamento_total] - [faturamento_mes_anterior],
    [faturamento_mes_anterior],
    "Mês Anterior Sem Vendas"
)
```
