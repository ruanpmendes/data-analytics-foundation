### Funções Lógicas e Matemática Avançada

#### **Utilização de `AND`, `OR` no Excel**

> No Excel, as funções com sufixo IFS (como SUMIFS e COUNTIFS) trabalham nativamente com a lógica AND.

Contagem Inteligente com **`COUNTIFS`**

```
Sintaxe: =COUNTIFS(criterio_range1, criterio1, [criterio_range2, criterio2],...)
```

Exemplo Real com Operadores Matemáticos

Cenário Hipotético: Você tem uma tabela de notas fiscais e quer contar quantas notas da Região "Sul" tiveram um valor maior ou igual a 5000.

```
=COUNTIFS(Tabela[Região], "Sul", Tabela[Valor], ">=5000")
```

> Sempre que for usar operadores lógicos dentro de `IFS`, eles devem estar entre aspas duplas.

O Poder do **`IF`** com **`AND` / `OR`**

```
Sintaxe: =IF(condicao, valor_se_V, valor_se_F)
```

**Classificação com `AND`:** A empresa vai dar um bônus para os vendedores que bateram a meta e têm mais de 2 anos de casa. A fórmula na coluna de classificação seria:

```
=IF(AND([@Bateu_Meta]="Sim", [@Anos_Casa]>2), "Ganhou Bônus", "Sem Bônus")
```

**Classificação com `OR`:** A equipe de compliance quer mapear as transações suspeitas. Uma transação é suspeita se o valor for maior que 50K ou se o status do cadastro do cliente for incompleto.
A fórmula na coluna de tipo_transação seria:

```
=IF(OR([@Valor]>50000, [@Status]="Incompleto"), "Alerta", "Normal")
```

---

### **Exercícios:**

| Student       | Region  | Status    | Progress_Pct | Amount_Paid |
| ------------- | ------- | --------- | ------------ | ----------- |
| Ana Silva     | Norte   | Ativo     | 0.85         | 450         |
| Bruno Costa   | Sudeste | Cancelado | 0.2          | 0           |
| Carlos Souza  | Sul     | Ativo     | 0.95         | 600         |
| Daniela Lima  | Norte   | Pendente  | 0.1          | 450         |
| Eduardo Gomes | Sudeste | Ativo     | 0.4          | 350         |
| Fernanda Dias | Norte   | Ativo     | 0.75         | 500         |
| Gabriel Cruz  | Sul     | Cancelado | 0.05         | 0           |
| Helena Moura  | Sudeste | Ativo     | 0.9          | 600         |

##### 1. (`COUNTIFS` - Lógica `AND`): Quantos alunos são da região "Norte" E estão com o status "Ativo" ao mesmo tempo?

```
=COUNTIFS(Students[Region], "Norte", Students[Status], "Ativo")
```

##### 2. (`SUMIFS` - Operadores Matemáticos): Qual o valor total pago (Amount_Paid) apenas pelos alunos que tiveram um progresso (Progress_Pct) maior ou igual a 0.50 (50%)?

```
=SUMIFS(Students[Amount_Paid], Students[Progress_Pct], ">=0.5")
```

##### 3. (`IF` + `AND` - Nova Coluna): Crie uma nova coluna na tabela chamada [Certificate_Status]. Usando a função `IF` combinada com `AND`, a regra é: Se o aluno estiver "Ativo" E o progresso for maior ou igual a 0.80 (80%), a fórmula deve retornar "Elegível". Caso contrário, deve retornar "Não Elegível".

```
=IF(AND([@Status]="Ativo", [@[Progress_Pct]]>=0.8), "Elegível", "Não Elegível")
```

##### 4. (`IF` + `OR` - Nova Coluna): Crie outra coluna chamada [Attention_Flag]. Usando `IF` combinado com `OR`, a regra é: Se o status do aluno for igual a "Cancelado" **OU** o progresso dele for menor que 0.15 (15%), a fórmula deve retornar "Alerta", caso contrário, "Normal".

```
=IF(OR([@Status]="Cancelado", [@[Progress_Pct]]<0.15), "Alerta", "Normal")
```

> Dicas com relação aos exercícios 3 e 4:
>
> Sempre que o nome de uma coluna tiver espaços (ex: Preço Unitário) ou caracteres especiais (ex: Progress_Pct, Custo(R$)), o Excel vai exigir automaticamente esse "duplo colchete" `[@[Nome_Coluna]]` para proteger o nome da coluna.
