### ALL / ALLSELECTED

#### **ALL**

ALL retorna todas as linhas de uma tabela ou todas as céluas de uma coluna, desconsiderando qualquer filtro.

> Sintaxe **ALL**: `ALL(Tabela ou Coluna, [Coluna1], [Coluna2],...)`

> Só podemos adicionar novas colunas se o primeiro argumento foi uma coluna e não uma tabela:
>
> - Tabela: ALL(Vendas)
> - Coluna(s): ALL(dLojas[Pais], dLoja[Nome_Loja],...)

```
-- Achando o total de receita, removendo todos os filtros (de Clientes):
Total_Receita_Absoluta
CALCULATE(
    SUM(Vendas[Receita]),
    ALL(Clientes)
)

-- Calculando o percentual de cada cliente sobre a Receita Total:
%_Receita_Cliente =
DIVIDE([Total_Receita], [Total_Receita_Absoluta], 0)
```

**_Saída em uma matriz:_**

> Pode remover a coluna "Receita Absoluta" da matriz, mas para melhor entendimento, vou manter.

| Nome          | Receita | Receita Absoluta | % Receita |
| ------------- | ------- | ---------------- | --------- |
| Aroldo Gomes  | 10.780  | 183.967          | 5,86 %    |
| Susane Peres  | 7.567   | 183.967          | 4,11 %    |
| Ricardo Sales | 14.129  | 183.967          | 7,68 %    |
| ...           | ...     | ...              | ...       |

> Para funcionar para todas análises, ao invés de passar uma tabela dimensão como parâmetro, passar a tabela fato. No nosso exemplo acima ficaria: `ALL(Vendas)`, assim qualquer análise que fizer, ele vai calcular o **total** removendo todos os filtros.

#### **ALLSELECTED**

Para remover apenas os filtros de dentro da tabela/matriz, e aceitar filtros externos, como Segmentação de Dados, Clicks em Gráficos de colua/barra, usamos o **ALLSELECTED**.

> Mesma Sintaxe da fórmula ALL.

> Sintaxe **ALLSELECTED**: `ALLSELECTED(Tabela ou Coluna, [Coluna1], [Coluna2],...)`