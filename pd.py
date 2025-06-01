#%%

import pandas as pd


## -----------------------------------------------------------------------------------------------------------------------------

## Manipulando Dados em DataFrames do Pandas

## Cria um dicionário

dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', ' Bahia', 'Minas Gerais'],
        'Ano': [2004, 2005, 2006, 2007, 2008],
        'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]
}

## Converter em um dataframe

df = pd.DataFrame(dados)

## Vizualizar as 5 primeiras linhas

df.head()

## Tipo

type(df) ## -> pandas.core.frame.DataFrame -> TABELA

## Reorganizar a ordem das colunas

pd.DataFrame(dados, columns= ['Estado', 'Taxa Desemprego', 'Ano'])

## Criando outro dataframe com os mesmos dados mas adicionando uma coluna

df2 = pd.DataFrame(dados, columns= ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'], 
                   index= ['Estado1', 'Estado2', 'Estado3', 'Estado4', 'Estado5'])
df2

## Imprimir as colunas

df2.columns ## -> Index(['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'], dtype='object')

## Imprimir valores do dataframe

df2.values

## Imprimir os tipos

df2.dtypes

## Imprimindo apenas uma coluna do DataFrame

df2['Estado']

## Imprimindo apenas duas colunas do DataFrame

df2[['Taxa Desemprego', 'Ano']]

## Imprimir os index

df2.index ## -> Index(['Estado1', 'Estado2', 'Estado3', 'Estado4', 'Estado5'], dtype='object')]

## Filtrando um DataFrame pelo index

df2.filter(items= ['Estado3'], axis=0)

## --------------------------------------------------------------------------------------------------------------------------

## Usando NumPy e Pandas para manipulação de dados

import numpy as np

df2.describe()

df2.isna()

## Usando NumPy para preencher valores NaN de uma coluna

df2['Taxa Crescimento'].isna()

df2['Taxa Crescimento'] = np.arange(5.)
df2

df2.dtypes
df2.describe()

## ------------------------------------------------------------------------------------------------------------------------------

## Silicing de DataFrames do Pandas

df2 = [df2['Estado2': 'Estado4']]

df2[ df2['Taxa Desemprego'] < 2]

df2[['Estado', 'Taxa Crescimento']]

## ---------------------------------------------------------------------------------------------------------------------------------

## Preenchendo valores Ausentes em DataFrames do Pandas

## Importando um dataset
df = pd.read_csv("dataset.csv")

df.head()

##

df.isna().sum

## Extrair a moda da coluna Quantity
## Value_counts() -> Conta quantas vezes cada valor aparece na coluna
## -> .index[0] -> Pega o valor com a maior frequência, ou seja, a moda

moda = df['Quantidade'].value_counts().index[0]

## Preencher os valores Na com a moda
## -> Inplace usado para salvar a alteração no próprio dataframe

df['Quantidade'].fillna(value= moda, inplace=True)

## -------------------------------------------------------------------------------------------------------------------------------------

## Query (Consulta) de Dados no DataFrame do Pandas
## Querys facilitam o uso de múltiplas condições e condições parecidas com a do SQL

df.Valor_venda.describe()

## Gerar um novo df apenas com os intervalos de vendas

df3 = df.query('229' < Valor_venda < '10000')
df3.Valor_venda.describe()

## Gerar um df com os valores de venda acima da média

df4 = df3.query('Valor_venda'> 766)

## ---------------------------------------------------------------------------------------------------------------------------------------

## Verificiando a Ocorrência de Diversos Valores em uma Coluna

## Método isin para filtrar todas as linhas da coluna "Quantidade", onde o valor é igual a 5,7,9,11
df[df['Quantidade'].isin([5,7,9,11])]

## ---------------------------------------------------------------------------------------------------------------------------------------

## Operadores lógicos para manipulação de Dados com Pandas

## Filtrando as vendas que ocorrem para os segmento "Home office" e na região "South"
## Usando operador lógico AND e retornar se as duas forem verdadeiras

df[(df.Segmento == 'Home Office') & (df.Regiao == 'South')].head()

## Checar e retornar se apenas uma delas for verdadeira

df[(df.Segmento == 'Home Office') | (df.Regiao == 'South')].tail()

## Chegar e retornar tudo que não for o segmento "Home office" e região "South"
## Os dois tem que ser diferentes de ambos os filtros

df[(df.Segmento != 'Home Office') & (df.Regiao != 'South')].sample(5)

## --------------------------------------------------------------------------------------------------------------------------------------

## Agrupamento de Dados em DataFrames com Group By

df.head()

## Filtramos as 3 colunas, e em sêquencia agrupamos elas por duas colunas, 'Segmento' e 'Regiao'.
## E então fazemos a média da coluna que ficou fora do groupby, nesse caso o 'valor_venda'

df[['Segmento', 'Regiao', 'Valor_venda']].groupby(['Segmento', 'Regiao']).mean()

## Agregaçãp Múltipla com group By

df[['Segmento', 'Regiao', 'Valor_venda']].groupby(['Segmento', 'Regiao']).agg('mean', 'std', 'count')


## --------------------------------------------------------------------------------------------------------------------------------------

## Filtrando DataFrame do Pandas com Base em Strings

df.head()

## Filtrando o dataFrame pela Coluna Segmento com valores que inicia com as letras 'Con'
df[df['Segmento'].str.startswith('Con')].head()

## Filtrando o dataFrame pela Coluna Segmento com valores que terminam com as letras 'mer'
df[df['Segmento'].str.endswith('mer')].head()

## Ambas as funções são uteis quando for necessário filtrar string por caracteres que apareçam no começo ou no final

## ------------------------------------------------------------------------------------------------------------------------------------------

## Split de Strins em DataFrames do Pandas

df['ID_Pedido'].head() ## -> formatato das colunas "Id_Pedido" -> CA-2016-152156 / US-2015-108966

## Split da coluna pelo caracter '-'

df['ID_Pedido'].str.split('-')  ## -> [CA, 2016, 152156] -> [US, 2015, 108966] ## Retorna uma lista de valores

df['Ano'] = df['ID_Pedido'].str.split('-').str[1].head() ## -> 2016, 2015 ## Ao usar o indice, agora retornar apenas os anos e armazena em uma coluna

## Strip de String em DataFrames do Pandas

df['Data_Pedido'].head() ## -> 2016-11-08

## Se por uma acaso for necessario deixar dois digitos na parte do ano, podemos usar o lstrip, ou seja, left strip

df['Data_Pedido'].str.lstrip('20') ## -> 16-11-8

## ----------------------------------------------------------------------------------------------------------------------------------------------

## Replace de String em DataFrames do Pandas

## Substiuir os caracteres CG por AX na coluna 'ID_clientes'

df['Id_Cliente'] = df['Id_Cliente'].str.replace('CG', 'AX')

## ---------------------------------------------------------------------------------------------------------------------------------------------

## Combinação de String em DataFrames do Pandas

## Concatenando Strings
## Cat, usado para juntar as duas strings e sep '-' para ter uma separação entre as duas strings das duas colunas

df['Pedido_Segmento'] = df['Id_Pedido'].str.cat(df['Segmento'], sep = '-')