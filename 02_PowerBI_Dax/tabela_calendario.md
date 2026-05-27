### Tabela Calendário com Linguagem M

#### Guia simplificado de como criar uma tabela calendário completa usando linguagem M.

#### **Passo a passo**

#### 1. Dentro do Power Query, clique em `Nova Fonte` > `Consulta Nula`.

#### 2. No terminal que abrir, digite `=List.Dates`.

#### 3. Apareceram 3 campos para preencher: `start`, `count` e `step`. Coloque qualquer data no `start`, qualquer número no `count` e 1 no `step`. Clique em `Invocar`.

- `start` - Primeira data da tabela calendário;
- `count` - Quantos dias a partir da primeira data vai conter na tabela.
- `step` - De quantos em quantos dias vai "pular", de 1 em 1 dias, de 2 em 2, etc.

#### 4. Na aba superior, vá para `Página Inicial` e clique em `Editor Avançado`.

#### 5. Após o `let` e antes de `Fonte`, vamos três variáveis, sendo elas: `PrimeiraData`, `UltimaData` e `TempoEntreDatas`. Para isso, na nossa tabela fato, deve conter uma coluna do tipo de `Data`. No exemplo, iremos utilizar a tabela `fVendas`, com a coluna `data_venda`.

```
-- O bloco de Editor Avançado deve ficar semelhante a isso:
let
    PrimeiraData = List.Min(fVendas[data_venda]),
    UltimaData = List.Max(fVendas[data_venda]),
    TempoEntreDatas = Duration.Days(UltimaData - PrimeiraData) + 1,
    Fonte = Consulta(PrimeiraData, TempoEntreDatas, #duration(1, 0, 0, 0))
in
    Fonte
```

Clique em `Concluído`.

**Glossário**

- `List.Min` => Lista a menor data da coluna `[data_venda]`.
- `List.Max` => Lista a maior data da coluna `[data_venda]`.
- `Duration.Days` => Calcula a diferença de dias entre a `UltimaData` e `PrimeiraData`.
- Somamos mais 1 no final, para acertar a quantidade de dias.
  Ex: A diferença de dias entre segunda e sexta é de 4 dias (5 - 1 = 4), se pegarmos 4 dias a partir de segunda ficaria: Segunda, Terça, Quarta e Quinta, faltaria a Sexta, por isso adicionamos + 1 no fim.

- Por fim, em `Fonte`, temos os parametros iniciais da função `List.Dates`, mas de forma inteligente, onde o `start` recebe `PrimeiraData`, `count` recebe `TempoEntreDatas` e o `step` mantemos o inicial, que é 1.

#### 6. Na aba superior, vá em `Transformar`, e clique no canto superior esquerdo em `Para a Tabela` > `Ok`.

#### 7. Altere o nome da coluna, nome da tabela e o tipo para Data.

---

**Até aqui sua tabela calendário está pronta. Se quiser pode clicar em `Fechar e Aplicar` e retornar para o Dashboard. Daqui em diante, é para elvarmos o nível da tabela, deixando ela mais robusta, para análises de data mais detalhadas.**

---

#### 8. Criação das colunas no Power Query.

Na aba `Adicionar Coluna` > `Data`, vamos criar as seguintes colunas:

1. `ano_num` com o número do ano apenas: `Data` > `Ano` > `Ano`.
2. `mes_num` com o número do mês: `Data` > `Mês` > `Mês`.
3. `mes_nome` com o nome do mês: `Data` > `Mês` > `Nome do Mês`.
4. `trimestre` com o número do trimestre no ano: `Data` > `Trimestre` > `Trimestre do Ano`.
5. `dia_num` com o número do dia na semana: `Data` > `Dia` > `Dia da Semana`.
6. `dia_nome` com o nome do dia: `Data` > `Dia` > `Nome do Dia`.

#### 9. Criação das colunas no DAX.

Em `Modo de exibição da tabela`, segunda aba do menu lateral esquerdo. Entre na tabela calendário. Clique em `Nova Coluna` e vamos criar mais 2 colunas importantes, principalmente se sua tabela/base de dados, possui datas de anos diferentes.

1. `mes_ano_num` com a junção entre o `ano_num` + `mes_nume`. O intuito é ficar assim o resultado, exemplo Janeiro de 2026 ficar "202601" e assim por diante.

   ```
   mes_ano_num =
   tabelaCalendario[ano_num] * 100 + tabelaCalendario[mes_num]

   -- Saida: 202601, 202602, ...
   ```

2. `mes_ano` com as três primeiras letras do mês + "/" + ano. exemplo de Janeiro de 2026, ficar "jan/2026". Fazendo assim, para relatório ficarem melhores visualmente.

   ```
   mes_ano =
   FORMAT(tabelaCalendario[data], "MMM/yyyy")

   -- Saída: jan/2026, fev/2026, ...
   ```

#### 10. Problema de ordenação dos meses/dias.

Por padrão, o Power BI ordena textos por ordem alfabética. No nosso caso, onde temos dados de texto como `dia_nome`, `mes_nome` ele ordenará da seguinte forma:

- `dia_nome`: `Domingo`, `Quarta-Feira`, `Quinta-Feira`, `Segunda-Feira`.
- `mes_nome`: `Abril`, `Agosto`, `Dezembro`, `Fevereiro`

Pensando nisso que criamos as colunas númericas `num`, como `dia_num`, `mes_num` e `mes_ano_num`. Elas servirão para ordenar de forma correta as nossas colunas de texto.

Para isso, continue em `Modo de exibição da tabela`, entre na tabelaCalendário. Na coluna `mes_nome` por exemplo, clique nela, e na aba superior tem uma função `Classificar por coluna`, clique nela e selecione a coluna `mes_num`. O Power BI agora, não classificará mais por ordem alfabética, ele vai classificar a coluna de acordo com a outra coluna `mes_num`, ou seja, agora, `Janeiro` será o 1° mês, `Fevereiro` o 2° e assim sucessivamente.

Para as demais colunas, aplicar a mesma lógica, ordenar pela coluna `num`.
