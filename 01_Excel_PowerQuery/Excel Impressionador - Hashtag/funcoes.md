## DATE

Para comparar datas no Excel, usamos a função `DATE(year;month;day)`.

> Ex: Comparar se a célula B2 é anterior a 31/12/2025:

```excel
IF(B2<DATE(2025;12;31);"Anterior";"Posterior")
```
---

## COUNTIFS

Conta quantas células do intervalo, correspondem ao valor do critério. Aceita vários intervalos e cirtérios.

> OBS: Para mais de um intervalo e critério, por padrão, funciona como um AND, todos os critérios tem que ser verdadeiros.

Ex 1: Contar quantos registros na coluna B, correspondem a cor digitada na coluna G1:

```excel
COUNTIFS(B:B;G1)
```

Ex 2: Contar quantos registros na coluna B, correspondem a cor digitada na coluna G1 E também ser do sexo "Feminino" (coluna C):

```excel
COUNTIFS(B:B;G1;C:C;"Feminino")
```

### Comparações dentro do COUNTIFS

> OBS: abaixo, utilizamos o operador lógico ">", mas pode ser qualquer outro!

> O caracter `&` concatena textos ou valores.

#### Pasando a data ou valor diretamente na função:

Utilizamos ">dd/mm/yyyy" ou ">2000".

Ex: Contar quantos funcionários foram contratados depois de 2024:

> COUNTIFS(E:E;">31/12/2024")

#### Pasando a data ou valor apontando para uma célula:

Utilizamos ">" & H2 ou ">" & C2.

Ex: Contar quantos funcionários foram contratados depois de 2024 (célula H2 tem a data 31/12/2024):

```excel
COUNTIFS(E:E;">" & H2)
```

> OBS:
> 
> Para buscar por textos não exatos, como o LIKE do SQL, no Excel, utilizamos o asterístico("*") ao invés de porcentagem("%").
>
> Ex: Para buscar a quantidade de funcionários com o cargo de "Analista...", faremos da seguinte forma:
> ```excel
> =COUNTIFS(B:B;"*Analista*")

---

## SUMIFS

Realiza a soma de um intervalo numérico com base em **um ou mais critérios** simultâneos (funciona como uma lógica `E` / `AND`).

### 📌 Sintaxe Geral
```excel
=SUMIFS(intervalo_soma; intervalo_critério1; critério1; [intervalo_critério2; critério2]; ...)
```
Ex: Somar qual foi o valor total de vendas, dos vendedores da equipe "Alpha" e que seja do sexo "Feminino".

```excel
SUMIFS(C:C;B:B;"Feminino";D:D;"Alpha")
```

> - C: Coluna do valor das vendas
> - B: Coluna do sexo dos funcionários
> - D: Coluna com o nome da equipe