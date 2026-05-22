### INDEX + MATCH e XLOOKUP

```
Sintaxe do tradicional VLOOKUP(PROCV): =VLOOKUP(valor_procurado,matriz_tabela,indice_coluna,[procurar_intervalo])`
```

**3 grandes Problemas do `VLOOKUP`:**

1. **_Limitação da esquerda:_** O `VLOOKUP` obriga que a coluna de busca, seja a primeira coluna à esquerda da tabela, se a coluna de busca for a C e você quiser trazer os dados da coluna B, o `VLOOKUP` não funciona!

2. **_INDEX de Coluna Engessado:_** O terceiro argumento, é um número fixo (ex: 3 para trazer a terceira coluna). Se amanhã um colega adicionar uma coluna na posição 2 por exemplo, a sua coluna 3, passa ser a 4, e o `VLOOKUP` vai continuar trazendo o dado da coluna 3, ou seja, trazendo o dado errado.

3. **_Performance Pesada:_** O `VLOOKUP` força o Excel a carregar a matriz inteira na memória. Em planilhas grandes, o desempenho dá máquina cai.

**Solução 1: (Solução Elegante: `INDEX`+`MATCH`)**

- `MATCH` = Em qual linha está o item que eu procuro?
- `INDEX` = Sabendo o nro da linha (e da coluna), qual o valor está la dentro?
  > O `MATCH` não traz o salário ou nome de ninguém. Ele traz apenas a posição (nro da linha) de um item na lista.

```
Sintaxe: =MATCH(oq_voce_busca, coluna_onde_está, 0) -- o 0 significa busca exata.
```

```
Sintaxe: =INDEX(coluna_com_resultado, nro_linha)
```

**Exemplo:**

Se buscarmos o ID "A123" na coluna de ID, o `MATCH` vai retornar, por exemplo, o nro 5, ou seja, significa que o ID "A123" está na 5ª linha de dados.O `INDEX` Faz o oposto. Você dá uma coluna e diz: "Me traz o que está na linha 5".

#### **Juntado as duas funções:**

Colocamos o `MATCH` dentro do `INDEX` para automatizar a descoberta da linha:

```
=INDEX(coluna_com_resultado, MATCH(oq_voce_busca, coluna_onde_está, 0))
```

#### **Por que isso resolve?**

Porque apontamos para duas colunas isoladas. Se alguém adicionar 10 colunas no meio da tabela, a coluna de busca e a coluna de resultado continuam a existindo de forma independente. A fórmula não quebra. Além disso, a coluna de resultado, pode estar à esquerda ou à direita.

---

**Solução 2: `XLOOKUP`**

```
Sintaxe: =XLOOKUP(lookup_value, lookup_array, return_array)
```

- `lookup_value` == O que estamos buscando
- `lookup_array` == Em qual coluna isolada esse valor está?
- `return_array` == De qual coluna você quer trazer o resultado

**Por que essa função é a melhor opção?**

- Busca para esquerda: A coluna retorno `return_array` pode estar em qualquer lugar, à esquerda ou à direita da coluna de busca.
- Inquebrável: Como apontamos para duas colunas separadas, se alguém adicionar ou deletar colunas no meio da tabela, o relatório continua intacto.
- Tratamento de erros nativos: O erro `#N/A`, no `XLOOKUP` tem um 4° argumento opcional `if_not_found`. Podemos escrever por exemplo `=XLOOKUP(A2, B:B, C:C, "Não Encontrado")`. Se ele não achar, já limpa o relatório para você sem precisar da função IFERROR por fora.

---

### **Exercícios:**

##### 1. Você recebeu uma tabela onde a chave de busca (o ID do Produto) está bem no meio da tabela, quebrando totalmente qualquer chance de usar o antigo `VLOOKUP`.

Fora da tabela, na célula F2, imagine que você digitou o código que quer buscar: PROD-441.
Agora, usando Referências Estruturadas, resolva as duas tarefas abaixo na planilha:

##### 1.1 Na célula G2, use a combinação `INDEX` + `MATCH` para descobrir o nome do produto (SKU_Name) olhando para o ID da célula F2. (Repare que o nome está à esquerda do ID!).

##### 1.2 Na célula H2, use o moderno `XLOOKUP` para descobrir o preço (Price) desse mesmo produto baseado na célula F2.

Amostra dos Dados
|SKU_Name |Product_ID |Price |Department
|-|-|-|-|
|Teclado Mecânico|PROD-992 |350 |Periféricos
|Mouse Gamer |PROD-105 |220 |Periféricos
|Monitor 24' |PROD-441 |1200 |Monitores
|Cadeira Office |PROD-302 |850 |Móveis
|Headset Wireless|PROD-884 |450 |Periféricos

```
1.1: =INDEX(Products[SKU_Name], MATCH(F2, Products[Product_ID], 0))
1.2: =XLOOKUP(F2, Products[Product_ID], Products[Price])
```

---

##### 2. O setor financeiro precisa descobrir o nome do fornecedor baseado no número da nota fiscal. O problema é que a coluna de busca está depois do nome do fornecedor.

Valor para procurar: NF-902. Use `INDEX` + `MATCH` para retornar o nome do fornecedor.

Amostra dos Dados
|Supplier |Invoice_Number |Total_Value
|-|-|-|
|TechCorp |NF-105 |15000
|LogiBrasil |NF-441 |8500
|OfficeDesign|NF-902 |12200
|Soluções TI |NF-302 |4300

```
=INDEX(Financials[Supplier], MATCH(G11, Financials[Invoice_Number], 0))
```

---

##### 3. Logística (Desafio do Tratamento de Erro do `XLOOKUP`)

Você precisa checar o status de entrega de um código de rastreio. Porém, alguns códigos digitados podem estar errados ou ainda não foram registrados no sistema.
Valor para procurar: BR-888 (Esse Código não existe na tabela, utilizar 4° parametros de `XLOOKUP`)

Amostra dos Dados
|Tracking_Code |Destination |Status
|-|-|-|
|BR-101 |São Paulo |Entregue
|BR-202 |Rio de Janeiro |Em Trânsito
|BR-303 |Belo Horizonte |Despachado
|BR-404 |Curitiba |Em Trânsito

```
=XLOOKUP(G18,Logistcs[Tracking_Code], Logistcs[Status], "Not found")
```
