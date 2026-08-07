## Intervalos Nomeados e Validação Dinâmica em Cascata

O uso de **Intervalos Nomeados** substitui referências de células genéricas (ex: `H2:H9`) por nomes amigáveis e estruturados. Quando combinado com a função `INDIRECT(INDIRETO)`, permite criar listas de validação em cascata (dependentes).

---

### 1. Como Criar um Intervalo Nomeado

- **Via Atalho:** Pressione `CTRL + F3` > Clique em **Novo (New)** > Digite o **Nome** > Selecione o intervalo de células desejado.
- **Via Caixa de Nome:** Selecione as células > Digite o nome na **Caixa de Nome** (no canto esquerdo da barra de fórmulas) > Pressione `ENTER`.

> **Aplicação:** Em formulários de Validação de Dados (Lista), em vez de passar `=H2:H9`, você passa apenas `=nome_do_intervalo`.

---

### 2. Validação de Dados Condicionada / Em Cascata

Usada para fazer com que as opções de uma Segunda Lista dependam da escolha feita na Primeira Lista (Ex: escolher o _Continente_ em `A2` e a lista de _Países_ se adaptar automaticamente em `B2`).

#### Passo a Passo:

1. Crie intervalos nomeados separados para os países de cada continente.
2. **Regra de Ouro:** O nome do intervalo deve ser **exatamente igual** ao texto que aparece na célula de seleção do continente (Atenção: nomes de intervalos não aceitam espaços, use underline `_`).
3. Na célula onde ficará a lista dependente de países, acesse **Validação de Dados** > Selecionar **Lista**.
4. Na fonte da lista, use a fórmula:
   ```excel
   =INDIRECT(A2)
   ```
   (A função INDIRECT lê o texto selecionado em A2 e o converte na referência do intervalo nomeado correspondente).

> Dica Pro: Automatização com Tabelas
> Para tornar a lista inteligente e reconhecer automaticamente novos itens adicionados aos intervalos nomeados, converta as listas de origem em Tabelas Oficiais (CTRL + ALT + T). Assim, qualquer novo item digitado no final da tabela expandirá o intervalo nomeado sem quebrar as fórmulas. Para funcionar de fato, troque a referência do intervalo nomeado, para o nome da tabela criada (ex: =paises_asia).

## Validação de Dados Avançada com Fórmulas Personalizadas

A **Validação de Dados por Fórmula Personalizada** permite criar travas de segurança dinâmicas em uma planilha, impedindo que o usuário insira valores que violem regras de negócio (como estourar um orçamento ou ultrapassar um limite).

---

### Estudo de Caso: Trava de Orçamento Salarial

#### Contexto:

Uma planilha contém a lista de salários dos funcionários, uma célula com o **Total Acumulado** e outra com o **Orçamento Máximo Permitido**. O objetivo é impedir a inserção ou aumento de salários que façam o total ultrapassar o orçamento.

#### Estrutura da Tabela (Exemplo):

Tabela:
| Funcionário | Salário |
|-|-|
|Arlindo|3.000|
|Rosa|5.000|
|Fred|2.500|
|...|...|
|...|...|
|...|...|
|Total de salários|10.500|
|Orçamento Máximo|15.000|

---

### Passo a Passo de Configuração:

1. Selecione o intervalo de células onde os dados serão digitados (ex: `B2:B7`).
2. Acesse a aba **Dados** > **Validação de Dados**.
3. Em _Permitir_, escolha **Personalizado** (no Google Sheets: _Fórmula personalizada é_).
4. Insira a fórmula de validação lógica:
   ```excel
   =$B$8 <= $B$9
   (Opcional) Configure a Mensagem de Erro (Aviso de Parada):
   ```

Título: "Limite de Orçamento Excedido"

Mensagem: "Este valor faz com que a folha salarial ultrapasse o orçamento máximo de R$ 15.000,00."

> Regra de Ouro do Trancamento: Como a validação é aplicada a um intervalo de várias células (B2:B7), é obrigatório trancar com cifrão ($B$8 <= $B$9) as células do Total e do Orçamento. Caso contrário, a validação mudará de linha à medida que avança pelas células do intervalo, gerando erros de checagem.
