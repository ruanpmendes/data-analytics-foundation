## DATE

Para comparar datas no Excel, usamos a função `DATE(year,month,day)`.

> Ex: Comparar se a célula B2 é anterior a 31/12/2025:

```excel
IF(B2<DATE(2025,12,31),"Anterior","Posterior")
```

---

## COUNTIFS

Conta quantas células do intervalo, correspondem ao valor do critério. Aceita vários intervalos e cirtérios.

> OBS: Para mais de um intervalo e critério, por padrão, funciona como um AND, todos os critérios tem que ser verdadeiros.

Ex 1: Contar quantos registros na coluna B, correspondem a cor digitada na coluna G1:

```excel
COUNTIFS(B:B,G1)
```

Ex 2: Contar quantos registros na coluna B, correspondem a cor digitada na coluna G1 E também ser do sexo "Feminino" (coluna C):

```excel
COUNTIFS(B:B,G1,C:C,"Feminino")
```

### Comparações dentro do COUNTIFS

> OBS: abaixo, utilizamos o operador lógico ">", mas pode ser qualquer outro!

> O caracter `&` concatena textos ou valores.

#### Pasando a data ou valor diretamente na função:

Utilizamos ">dd/mm/yyyy" ou ">2000".

Ex: Contar quantos funcionários foram contratados depois de 2024:

> COUNTIFS(E:E,">31/12/2024")

#### Pasando a data ou valor apontando para uma célula:

Utilizamos ">" & H2 ou ">" & C2.

Ex: Contar quantos funcionários foram contratados depois de 2024 (célula H2 tem a data 31/12/2024):

```excel
COUNTIFS(E:E,">" & H2)
```

> OBS:
>
> Para buscar por textos não exatos, como o LIKE do SQL, no Excel, utilizamos o asterístico("\*") ao invés de porcentagem("%").
>
> Ex: Para buscar a quantidade de funcionários com o cargo de "Analista...", faremos da seguinte forma:
>
> ```excel
> =COUNTIFS(B:B,"*Analista*")
> ```

---

## SUMIFS

Realiza a soma de um intervalo numérico com base em **um ou mais critérios** simultâneos (funciona como uma lógica `E` / `AND`).

### Sintaxe Geral

```excel
=SUMIFS(intervalo_soma, intervalo_critério1, critério1, [intervalo_critério2, critério2], ...)
```

Ex: Somar qual foi o valor total de vendas, dos vendedores da equipe "Alpha" e que seja do sexo "Feminino".

```excel
SUMIFS(C:C,B:B,"Feminino",D:D,"Alpha")
```

> - C: Coluna do valor das vendas
> - B: Coluna do sexo dos funcionários
> - D: Coluna com o nome da equipe

---

## AVERAGEIFS

Calcula a **média** de um intervalo numérico com base em **um ou mais critérios** simultâneos (lógica `E` / `AND`).

### Sintaxe Geral

```excel
=AVERAGEIFS(intervalo_média, intervalo_critério1, critério1, [intervalo_critério2, critério2], ...)
```

Ex: Média das vendas dos vendedores da equipe "Alpha" e sexo "Feminino".

```excel
=AVERAGEIFS(C:C,B:B,"Feminino",D:D,"Alpha")
```

> - C: Coluna do valor das vendas (intervalo a ser mediado)
> - B: Coluna do sexo
> - D: Coluna da equipe

---

## MAXIFS

Retorna o **maior valor** de um intervalo numérico com base em **um ou mais critérios** simultâneos (lógica `E` / `AND`).

### Sintaxe Geral

```excel
=MAXIFS(intervalo_máx, intervalo_critério1, critério1, [intervalo_critério2, critério2], ...)
```

Ex: Maior venda dos vendedores da equipe "Alpha" e sexo "Feminino".

```excel
=MAXIFS(C:C,B:B,"Feminino",D:D,"Alpha")
```

> - C: Coluna do valor das vendas (intervalo a avaliar o máximo)
> - B: Coluna do sexo
> - D: Coluna da equipe

---

## MINIFS

Retorna o **menor valor** de um intervalo numérico com base em **um ou mais critérios** simultâneos (lógica `E` / `AND`).

### Sintaxe Geral

```excel
=MINIFS(intervalo_mín, intervalo_critério1, critério1, [intervalo_critério2, critério2], ...)
```

Ex: Menor venda dos vendedores da equipe "Alpha" e sexo "Feminino".

```excel
=MINIFS(C:C,B:B,"Feminino",D:D,"Alpha")
```

> - C: Coluna do valor das vendas (intervalo a avaliar o mínimo)
> - B: Coluna do sexo
> - D: Coluna da equipe

---

### Padrão comum (\*IFS)

| Função       | O que faz no intervalo filtrado |
| ------------ | ------------------------------- |
| `SUMIFS`     | Soma                            |
| `AVERAGEIFS` | Média                           |
| `MAXIFS`     | Maior valor                     |
| `MINIFS`     | Menor valor                     |

Sintaxe compartilhada: **primeiro o intervalo de cálculo**, depois pares `intervalo_critério, critério` (todos os critérios precisam ser verdadeiros ao mesmo tempo).

---

## VLOOKUP (PROCV)

Busca um valor na **primeira coluna** de uma tabela e retorna o valor de outra coluna na mesma linha.

### Sintaxe Geral

```excel
=VLOOKUP(valor_procurado, matriz_tabela, núm_coluna, [procurar_intervalo])
```

Ex: Buscar o preço do produto "P001" na coluna 3 da tabela `A:C`.

```excel
=VLOOKUP("P001",A:C,3,0)
```

> - `0` / `FALSO` → correspondência **exata**
> - `1` / `VERDADEIRO` → correspondência **aproximada**: o Excel percorre a 1ª coluna (precisa estar ordenada crescente) e devolve a linha do **maior valor que ainda seja ≤ ao valor procurado** (“maior dentre os menores ou iguais”)

### VLOOKUP com chave composta

O `VLOOKUP` só procura na **primeira coluna** da matriz. Quando a busca depende de **dois (ou mais) campos ao mesmo tempo**, junta-se esses campos numa coluna auxiliar à esquerda da tabela.

#### Como montar

Na coluna mais à esquerda da matriz (ex.: coluna A), criar a **chave composta** concatenando os campos com `&`:

```excel
=B2&C2
```

No `VLOOKUP`, concatenar os mesmos campos, **na mesma ordem**, e usar correspondência exata (`0`):

```excel
=VLOOKUP(F5&G5,A:F,3,0)
```

> - A: coluna da chave composta (precisa ser a 1ª da matriz)
> - `F5&G5`: valor procurado (mesmos campos da chave, mesma ordem)
> - `A:F`: matriz; a busca acontece só na coluna A
> - `3`: coluna do resultado (contando a partir de A)
> - `0`: correspondência exata

Dica: se dois pares diferentes puderem virar o mesmo texto (ex.: `12`+`3` e `1`+`23`), use um separador: `=B2&"|"&C2` e `=VLOOKUP(F5&"|"&G5,A:F,3,0)`.

---

### VLOOKUP + COUNTIFS (vários resultados)

O `VLOOKUP` devolve **só a primeira** linha que bate. Se o mesmo nome pode aparecer mais de uma vez (ex.: vários "João Felix") e é preciso trazer **todos** (Estado, Telefone, …), numera-se cada ocorrência e busca-se `nome` + `número`.

#### 1. Coluna Repetição

Na tabela-base, contar quantas vezes o nome já apareceu **até a linha atual** (intervalo que cresce):

```excel
=COUNTIFS($D$2:D2,D2)
```

Copiar para baixo. Na linha 9 fica `$D$2:D9` (início trancado, fim da linha atual). Resultado:

| Repetição | Nome       |
| --------- | ---------- |
| 1         | João Felix |
| 1         | Rita de Sá |
| 2         | João Felix |

> `$D$2` trava o início; `D2` (sem `$` no fim) acompanha a linha. Sem o intervalo crescente, todos os João receberiam o mesmo número e a chave não distinguiria as linhas.

#### 2. Chave composta

À esquerda da matriz, juntar `nome` + `repetição` (mesmo padrão da anotação anterior):

```excel
=D2&C2
```

Ex.: `João Felix1`, `Rita de Sá1`, `João Felix2`.

#### 3. Área de busca (coluna Repetição oculta)

Onde se informa o nome procurado, criar uma coluna auxiliar com `1`, `2`, `3`… (pode ficar oculta). Cada linha faz um `VLOOKUP` da chave `nome&repetição`:

```excel
=VLOOKUP($F$5&G5,A:F,3,0)
```

> - `$F$5`: nome buscado (trancado, igual em todas as linhas)
> - `G5`: 1, 2, 3… (a coluna oculta; **não** trancar, para percorrer as ocorrências)
> - `3`: coluna do Estado (outro `VLOOKUP` na coluna do Telefone)

Quando não houver mais aquele número, o `VLOOKUP` quebra (`#N/A`). Para esconder o erro:

```excel
=IFERROR(VLOOKUP($F$5&G5,A:F,3,0),"")
```

Preencher linhas da área de busca até um número maior que o máximo de homônimos esperado.

---

## Uso do \* com FUNÇÕES (COUNTIFS, SUMIFS, VLOOKUP, etc)

Funciona de forma semelhante ao porcentagem (%) do SQL, na busca de valores.

por exemplo: Contar quantos produtos que começam com "Smart TV"

```excel
=COUNTIFS(Tabela[Produtos],"Smart TV*")
```

para produtos que terminem com "4K"

```excel
=COUNTIFS(Tabela[Produtos],"*4K")
```

para produtos que contém a palavra "Full HD"

```excel
=COUNTIFS(Tabela[Produtos],"*Full HD*")
```

---

## HLOOKUP (PROCH)

Busca um valor na **primeira linha** de uma tabela e retorna o valor de outra linha na mesma coluna.

### Sintaxe Geral

```excel
=HLOOKUP(valor_procurado, matriz_tabela, núm_linha, [procurar_intervalo])
```

Ex: Buscar o preço do produto "P001" na linha 3 da tabela `1:8`.

```excel
=HLOOKUP("P001",1:8,3,0)
```

---

## XLOOKUP (PROCX)

Busca um valor em um intervalo e devolve o valor correspondente de **outro intervalo** (mesma posição). Diferente do `VLOOKUP`: não precisa da coluna de busca à esquerda, não usa número de coluna e o padrão já é correspondência **exata**.

### Sintaxe Geral

```excel
=XLOOKUP(valor_procurado, intervalo_busca, intervalo_retorno, [se_não_encontrado], [modo_correspondência], [modo_pesquisa])
```

Ex: Buscar o preço do produto "P001" (nomes em `A:A`, preços em `C:C`).

```excel
=XLOOKUP("P001",A:A,C:C,"Não encontrado")
```

> - `intervalo_busca` e `intervalo_retorno` são intervalos **separados** (podem estar em qualquer ordem na planilha, inclusive retorno à esquerda da busca)
> - `se_não_encontrado`: texto/valor se não achar (substitui o `IFERROR` do `VLOOKUP`)
> - sem o 5º parâmetro → correspondência **exata** (equivalente ao `0` do `VLOOKUP`)

### 5º parâmetro — modo_correspondência

| Valor | Comportamento                                                                                                                                         |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | Exato (padrão)                                                                                                                                        |
| `-1`  | Exato ou o **maior valor ≤ ao procurado** (mesmo raciocínio do `VLOOKUP` com `1` / `VERDADEIRO`; intervalo de busca precisa estar ordenado crescente) |
| `1`   | Exato ou o **menor valor ≥ ao procurado**                                                                                                             |
| `2`   | Curinga (`*` e `?`)                                                                                                                                   |

### 6º parâmetro — modo_pesquisa (opcional)

> - `1` (padrão): começa do **início** do intervalo
> - `-1`: começa do **fim** (útil para pegar a última ocorrência)

Chave composta no `XLOOKUP` segue a mesma ideia do `VLOOKUP`: concatenar no valor procurado e no intervalo de busca (`=XLOOKUP(F5&G5,A:A,C:C)`), sem obrigar a chave a ser a primeira coluna da tabela.

---

### XLOOKUP duplo e triplo (vários critérios, sem coluna auxiliar)

O `XLOOKUP` simples busca em **um** intervalo. Para exigir **dois ou três critérios ao mesmo tempo** (lógica `E` / `AND`), multiplica-se comparações: cada uma vira `VERDADEIRO`/`FALSO` (`1`/`0`). O produto só é `1` quando **todas** as condições são verdadeiras.

O `1` no 1º argumento **não** é um modo da função: é o **valor procurado**. O Excel monta um vetor de `0` e `1` e o `XLOOKUP` procura o primeiro `1` (primeira linha em que todas as regras bateram).

### Duplo

```excel
=XLOOKUP(1,(B7:B405=B4)*(C7:C405=A4),D7:D405,"Não Encontrado")
```

> - `(B7:B405=B4)`: 1 onde a coluna B é igual a `B4`
> - `(C7:C405=A4)`: 1 onde a coluna C é igual a `A4`
> - `*` : só fica 1 se as duas forem 1 (`1*1=1`; qualquer `0` zera a linha)
> - `D7:D405`: valor a devolver (mesmo tamanho dos intervalos de busca)

### Triplo

```excel
=XLOOKUP(1,(B7:B405=B4)*(C7:C405=A4)*(A7:A405=C4),D7:D405,"Não Encontrado")
```

Mesma lógica: mais um `(intervalo=critério)` multiplicado. Só a linha em que as **três** comparações são verdadeiras gera `1`.

> Os três intervalos (`B7:B405`, `C7:C405`, `A7:A405`) e o retorno (`D7:D405`) precisam ter **o mesmo número de linhas**.

Devolve só a **primeira** linha que atende a todos os critérios (como o `XLOOKUP` normal). Para a última, usar o 6º parâmetro `-1`. Não substitui a técnica `COUNTIFS` + chave quando for preciso listar **todas** as ocorrências.

---

## MATCH (CORRESP)

Não devolve o valor da célula: devolve a **posição** (1ª, 2ª, 3ª…) do item dentro do intervalo.

### Sintaxe Geral

```excel
=MATCH(valor_procurado, intervalo_busca, [tipo_correspondência])
```

Ex: Em que linha (dentro de `A2:A100`) está o produto "P001".

```excel
=MATCH("P001",A2:A100,0)
```

> - `0` → correspondência **exata** (o mais usado)
> - `1` → maior valor **≤** ao procurado (intervalo precisa estar em ordem crescente; mesmo raciocínio do `VLOOKUP` com `1` / `VERDADEIRO`)
> - `-1` → menor valor **≥** ao procurado (intervalo em ordem decrescente)

O número retornado é relativo ao intervalo, não ao número da linha da planilha. Se a busca começa em `A2` e o item está em `A5`, o `MATCH` devolve `4`.

---

## INDEX (ÍNDICE)

Devolve o valor que está numa **posição** (linha e, se quiser, coluna) dentro de um intervalo.

### Sintaxe Geral

```excel
=INDEX(intervalo, núm_linha, [núm_coluna])
```

Ex: 3º valor da coluna de preços `C2:C100`.

```excel
=INDEX(C2:C100,3)
```

> - `núm_linha`: qual linha **dentro do intervalo** (1 = primeira célula do intervalo)
> - `núm_coluna`: só precisa se o intervalo tiver mais de uma coluna

Sozinho, o `INDEX` só funciona se você **já souber** o número da posição. Quase sempre ele entra junto com o `MATCH`.

---

## INDEX + MATCH

O `MATCH` acha a posição; o `INDEX` pega o valor nessa posição. Juntos substituem o `VLOOKUP`, com a vantagem de a coluna de busca **não** precisar estar à esquerda.

```excel
=INDEX(intervalo_retorno, MATCH(valor_procurado, intervalo_busca, 0))
```

Ex: Preço (`C:C`) do produto cujo código está em `A:A`.

```excel
=INDEX(C:C, MATCH("P001",A:A,0))
```

> - `MATCH("P001",A:A,0)` → posição da linha do "P001"
> - `INDEX(C:C, …)` → valor dessa mesma posição na coluna C
> - os dois intervalos devem ter o **mesmo tamanho** e começar na **mesma linha** (senão a posição aponta para a célula errada)

### Duas dimensões (linha e coluna)

Um `MATCH` para a linha e outro para a coluna:

```excel
=INDEX(B2:F10, MATCH("P001",A2:A10,0), MATCH("Jan",B1:F1,0))
```

> - 1º `MATCH`: em qual **linha** está "P001"
> - 2º `MATCH`: em qual **coluna** está "Jan"
> - `INDEX` cruza os dois e devolve a célula

Chave composta: o `MATCH` também aceita concatenação (`=MATCH(F5&G5,A:A,0)`), no mesmo espírito do `VLOOKUP` / `XLOOKUP`.
