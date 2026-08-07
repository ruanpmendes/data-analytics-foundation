## DATE

Para comparar datas no Excel, usamos a função `DATE(year;month;day)`.

> Ex: Comparar se a célula B2 é anterior a 31/12/2025:
>
> - IF(B2<DATE(2025;12;31);"Anterior";"Posterior")

---

## COUNTIFS

Conta quantas células do intervalo, correspondem ao valor do critério. Aceita vários intervalos e cirtérios.

> OBS: Para mais de um intervalo e critério, por padrão, funciona como um AND, todos os critérios tem que ser verdadeiros.

Ex 1: Contar quantos registros na coluna B, correspondem a cor digitada na coluna G1:

> COUNTIFS(B:B;G1)

Ex 2: Contar quantos registros na coluna B, correspondem a cor digitada na coluna G1 E também ser do sexo "Feminino" (coluna C):

> COUNTIFS(B:B;G1;C:C;"Feminino")

#### Comparações dentro do COUNTIFS

Para comparar datas ou valores, utilizamos ">dd/mm/yyyy" ou ">2000".

Ex: Contar quantos funcionários foram contratados depois de 2024:

> COUNTIFS(E:E;">31/12/2024")

---
