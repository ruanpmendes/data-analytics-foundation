### CALCULATE + FILTER

> **_Calculate_** é a fórmula mais **_importante_** do Power BI

### Tabelas de Amostras

##### Clientes

| ID_Cliente | Nome          | Segmento | Região       |
| ---------- | ------------- | -------- | ------------ |
| 091        | Aroldo Gomes  | Varejo   | Sul          |
| 852        | Susane Peres  | Varejo   | Sudeste      |
| 941        | Ricardo Sales | Online   | Centro-Oeste |
| ...        | ...           | ...      | ...          |

---

##### Vendas

| ID_Venda | ID_Cliente | ID_Produto | Data       | Quantidade | Receita | Lucro  |
| -------- | ---------- | ---------- | ---------- | ---------- | ------- | ------ |
| 1234     | 091        | 3          | 21/02/2026 | 3          | 795,18  | 195,56 |
| 4252     | 852        | 13         | 21/02/2026 | 4          | 737,80  | 156,86 |
| 2346     | 941        | 56         | 21/02/2026 | 2          | 1075,64 | 359,78 |
| ...      | ...        | ...        | ...        | ...        | ...     | ...    |

```
lucro_total = SUM(Vendas[Lucro])
```

```
qtd_clientes = COUNTROWS(Clientes)
```

Quando vamos filtrar por uma coluna da tabela, dá para passar no 2° paramêtro o que deve filtrar.

```
-- Quantos clientes do varejo?
qtd_clientes_varejo =
CALCULATE(
    [qtd_clientes],
    Clientes[Segmento] = "Varejo"
)
```

Mas quando vamos filtra por uma medida, e não coluna, devemos utilizar o FILTER

> Sintaxe do **FILTER**: `FILTER(Tabela, Expressão)`
>
> FILTER é uma fórmula **ITERADORA**, olha _linha_ a _linha_.

```
-- Quantos clientes trouxeram +10K de lucro?
qtd_clientes_10k+ =
CALCULATE(
    [qtd_clientes],
    FILTER(
        Clientes,
        [lucro_total] >= 10000
    )
)
```