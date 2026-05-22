### Pivot Table (Tabela Dinâmica)

**_Problema_**:

Temos uma tabela com o histórico de 10K vendas de uma loja. Cada linha é uma venda. Se o chefe perguntar: "Qual o total vendido por categoria em cada região?", precisariamos cruzar dados de várias colunas na fórmula.

A `Pivot Table` faz esse cruzamento, cruzando 4 quadrantes principais:

- `Rows`: O que queremos analisar na vertical (ex: Categorias)
- `Columns`: O que queremos cruzar na horizontal (ex: Regiões)
- `Values`: O que queremos calcular (Ex: Soma, Média, Quantidade)
- `Filters`: Regras para isolar o relatório inteiro

#### **Agrupamento de Datas Automático**

No Excel(Desktop), quando criamos uma Pivot Table, e arrastamos um campo de data para ela, ele agrupa automaticamente as datas em Anos, Trimestres, Meses.
Não havendo a necessidade de fazer essas colunas separadamente.

#### **Campos Calculados**

Imagine que na tabela original, temos as colunas Revenue e Cost. O gestor pede para mostrar no relatório dinâmico a margem de lucro e a comissão de 5% dos vendedores.
Um erro é voltar na tabela original, criar novas colunas com fórmulas e atualizar a `Pivot Table`. Isso pesa mais no arquivo e gasta memória.

A solução é criarmos um Campo Calculado diretamente na memória da Pivot Table.

```
1. Clica na Pivot Table > Pivot Table Analyze > Fields, Items & Sets > Calculated Field
2. Nomear a nova métrica
3. Digitar a fórmula usando os campos da própria tabela: "=Revenue - Cost" ou "=Revenue \* 0.05"
```

Essa nova coluna passa a existir apenas no resumo e se recalcula instantaneamente conforma mudamos o cruzamento de linhas e colunas.

#### **Segmentação de Dados**

Os filtros tradicionais de Tabela Dinâmica ficam escondidos no topo da planilha em um menu cascata cinza. Para deixar mais visual e interativo, usamos os Segmentos de Dados(Slicers). Transforma os filtros em botões flutuantes.

```
1. Clica na Pivot Table > Analyze > Insert Slicer
2. Escolhe o campo para ser o filtro.
```

O Excel vai gerar uma caixinha com os botões relacionados ao filtro. Quando o user clicar em um dos botões, o relatório todo filtra.

> OBSERVAÇÕES DE AMBIENTE (Excel WEB vs. DESKTOP):

- Os menus `Pivot Table Analyze` e `Analyze` mudam de nome na versão Web (navegador) para apenas uma aba verde chamada "PivotTable".
- Campos Calculados (Calculated Fields) são um recurso exclusivo do Excel Desktop (não funcionam na versão Web).
- O Agrupamento de Datas na versão Web não é automático ao arrastar; é necessário clicar com o botão direito em uma data dentro do relatório e selecionar a opção "Group".
