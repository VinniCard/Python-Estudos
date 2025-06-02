#%%

## Matplotlib e Seaborn ##

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


## Contruindo Plots
## Plot é uma representação gráfica de dados em uma figura. Em outras palavras, é um gráfico que mostrar a relação entre uma ou
## mais varíaveis.

## O método Plot() define os eixos do gráfico

plt.plot([1,3,5], [2,4,7])
plt.show()

## Criação de um gráfico a partir de uma lista

x = [2,3,5]
y = [3,5,7]

plt.plot(x,y)
plt.xlabel('Variavel 1') ## Definir o rótulo do eixo x
plt.ylabel('Variavel 2') ## Definir o rótulo do eixo y
plt.title('Teste Plot') ## Título do gráfico
plt.show()

##

x2 = [1,2,3]
y2 = [11,12,15]

plt.plot(x2, y2, label = 'Gráfico com Matplotlib')
plt.legend() ## -> texto passando no label, diretamente no plot, é usado para criar uma legenda para esse gráfico
plt.show()

## -------------------------------------------------------------------------------------------------------------------------------------

## Gráfico de Barras
## Usando para representar dados categóricos com barras retangulares.
## Cada barra representa uma categoria e a altura da barra representa a quantidade ou frenquência da categoria.
## O eixo horizontal (x), mostra as categorias. Enquanto o eixo vertica(y) mostra a escala da medida dos dados
## As barras podem ser vertical ou horizontal, dependendo da préferencia do usuário
## Muito usados para comparar quantidas ou frenquência de diferentes categorias. Úteis para mostrar diferenças entre grupos.

x1 = [2,4,6,8,10]
y1 = [6,7,8,2,4]

plt.bar(x1, y1, label = 'Barras', color = 'green')
plt.legend()
plt.show()

##

x3 = [1,3,5,7,9]
y3 = [7,8,2,4,2]

plt.bar(x1, y1, label = 'Listas1', color = 'blue')
plt.bar(x3, y3, label = 'Listas2', color = 'red')
plt.legend()
plt.show

##

idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]

ids = [x for x in range(len(idades))] ## Para cada número em range (tamanho) da lista, salve esse valor em ids 
    ## -> [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] -> Índices

plt.bar(ids, idades)
plt.show

## 

bins = [0,10,20,30,40,50,60,70,80,90,100,110,110,120,130]

plt.hist(idades, bins, histtype= 'bar', rwidth = 0.8) ## row width -> largura da linha
plt.show

plt.hist(idades, bins, histtype= 'stepfilled', rwidth = 0.8) ## row width -> largura da linha
plt.show

## ----------------------------------------------------------------------------------------------------------------------------------------

## Gráfico de Dispersão
## Usado para representar a relação entre duas variáveis contínuas. Sendo que, cada ponto representa um part de valores de duas variáveis
## Principalmente usado com variáveis númericas e se é preciso verificar se há correlação entre as variáveis

x4 = [1,2,3,4,5,6,7,8]
y4 = [5,2,4,5,6,8,4,8]

plt.scatter(x4, y4, label ='Pontos', color = 'black', marker = 'o')
plt.legend()
plt.show()

## ---------------------------------------------------------------------------------------------------------------------------------------

## Gráfico de Área Empilhada
## Usados para vizualizar a mudança relativa de diversas variáveis ao londo do tempo.
## São várias áreas coloridas empilhadas umas sobre as outras, onde a altura de cada área representa a magnitude da variável correspondente
## e a largura representa a escala de tempo
## Principalmente usado para mostrar com as partes contribuem para o todo ao longo do tempo. Podem ser usados para mostrar a mudança relativa
## de diferentes setores de uma indústria ao londo do tempo. Ou a distribuição relativa de receitas e despesas de uma empresa em um determinado
## período


dias = [1,2,3,4,5]
dormir = [7,8,9,6,7]
comer = [2,3,4,5,6]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors= ['m', 'c', 'r', 'k', 'b'])
plt.show()

## ---------------------------------------------------------------------------------------------------------------------------------------

## Gráfico de Pizza
## Representa a composição de uma variável categórica em relaçao ao todo.
## Cada fatia corresponde a uma categoria e sua área é proporcional à porcentagem que a categoria representa do todo.
## Por exemplo, usado para mostrar a distribuição de vendas por produto em uma emrpesa 

fatias = [7,2,2,13]
atividades = ['dormir','comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']

plt.pie(fatias, labels = atividades, colors = cores, startangle= 90, shadow= True, explode= (0,0.2,0,0))
plt.show()

##  explode -> usado para destacar (afastar) uma ou mais fatias da pizza
## startangle -> usado para definir o ângulo que o gráfico de pizza começa a ser desenhado

## -------------------------------------------------------------------------------------------------------------------------------------

## Criando gráficos customizados com Pylab
## Pylab é um módulo fornecido pela biblioteca Matplotlib
## Fornece um ambiente de plotagem interativo, permitindo criar gráficos de forma rapida e vizualizações de dados
## Combina também a funcionalidade do pacote NumPy com a funcionalidade do pacote 

import matplotlib_inline
import pylab
import numpy as np

## Gráfico de linha
## Usado para representar a evolução do comportado de uma variável com diferentes pontos de dados
## Cada ponto de dados é representado por um ponto na linha

## Dados
x5 = np.linspace(0, 5, 10)
y5 = x5 ** 2

## Cria a figura
fig = plt.figure() ## Figura é o todo, nele pode ter vários axes

## Define a escala dos eixos
axes = fig.add_axes([0, 0, 0.8, 0.8]) ## -> axes é o espaço onde o gráfico acontece

## Cria o plot
axes.plot(x5 ,y5, 'r') 

# Labels e título
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha')

## Gráfico de linha com 2 figuras

x5 = np.linspace(0, 5, 10)
y5 = x5 ** 2

fig = plt.figure() ## Figura é o todo, nele pode ter vários axes

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) ## -> axes é o espaço onde o gráfico acontece
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) ## -> axes é o espaço onde o gráfico acontece

axes1.plot(x5, y5, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

axes2.plot(y5, x5, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária')

## Gráficos de linha em Paralelo

x5 = np.linspace(0, 5, 10)
y5 = x5 ** 2

fig, axes = plt.subplots(nrows = 1, ncols = 2) ## -> usado quando trabalhado com mais de 1 gráfico em uma figura

for ax in axes:
    ax.plot(x5, y5, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')

fig.tight_layout()

## Gráfico de linha com diferentes escalas

x5 = np.linspace(0, 5, 10)
y5 = x5 ** 2

## Subplots
fig, axes = plt.subplots(1, 2, figsize=(10,4)) ## -> usado quando trabalhado com mais de 1 gráfico em uma figura

## Plot 1
axes[0].plot(x5, x5 **2, x5, np.exp(x5))
axes[0].set_title('Escala Padrão')

## Plot 2
axes[1].plot(x5, x5 **2, x5, np.exp(x5))
axes[1].set_yscale('log')
axes[1].set_title('Escala Logaritimica (y)')

## Grid

## Dados

x5 = np.linspace(0, 5, 10)
y5 = x5 ** 2

fig, axes = plt.subplots(1, 2, figsize=(10,3)) ## -> usado quando trabalhado com mais de 1 gráfico em uma figura

## Grid padrão
axes[0].plot(x5, x5 **2, x5, lw = 2)
axes[0].grid(True)

## Grid customizado
axes[1].plot(x5, x5 **2, x5, lw = 2)
axes[1].grid(color = 'b', alpha = 0.7, linestyle = 'dashed', linewidth = 0.8)

## ---------------------------------------------------------------------------------------------------------------------------------------

## Histogramas
## Usado para vizualizar a distribuição de uma variável contínua
## O eixo horizontal representa os intervalos de classe, enquanto o eixo vertical representa a frequência de observações de dados que
## caem em cada intervalo de classe.
## Úteis para vizualizar a forma e a dispersão de uma distribuição de dados contínuos.

## Dados

n = np.random.randn(100000)

fig, axes = plt.subplots(1, 2, figsize = (12,4)) ## -> 1 linha e 2 colunas ## -> usado quando trabalhado com mais de 1 gráfico em uma figura

## Plot 1

axes[0].hist(n)
axes[0].set_title('Histograma Padrão')
axes[0].set_xlim(min(n), max(n)) ## -> Define os limites do eixo x para ir desde o menor até o maior valor de "N"

## Plot 2

axes[1].hist(n, cumulative = True, bins = 50) ## -> Mostra a soma dos dados até atingir 100% dos dados (acumulativo)
axes[1].set_title('Histograma Cumulativo')
axes[1].set_xlim(min(n), max(n))

## --------------------------------------------------------------------------------------------------------------------------------------

## Seaborn
## Criando gráficos com Seaborn

import seaborn as sea

dados = sea.load_dataset("tips")

dados.head()

## O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados

sea.jointplot(data = dados, x = 'total_bill', y = 'tip', kind = 'reg')

## o método lmplot() cria plot com dados e modelos de regressão

sea.lmplot(data = dados, x = 'total_bill', y= 'tip', col = 'smoker')

##

df = pd.DataFrame()

df['idade'] = np.random.randint(20,100,30)
df['peso'] = np.random.randint(55,130,30)

sea.lmplot(data = df, x = 'idade', y = 'peso', fit_reg = True)

## Kdeplot

sea.kdeplot(df.idade)

## Kdeplot

sea.kdeplot(df.peso)

## Distplot

sea.distplot(df.peso)

## Histograma

plt.hist(df.idade, alpha = .3)
sea.rugplot(df.idade)

## BoxPlot

sea.boxplot(df.idade, color ='m')

## Vilon Plot

sea.violinplot(df.idade, color = 'g')

## Clustermap

sea.clustermap(df)

## --------------------------------------------------------------------------------------------------------------------------------------

## Matplotlib, Seaborn, Numpy e Pandas na Criação de Gráfico Estatístico

np.random.seed(42)
n = 1000 ## 1000 linhas ou 1000 pessoas
pct_smokers = 0.2

## np.random.rand -> Gera n números aleatórios entre 0 e 1
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n) ## Idades com média 40 e desvio padrão 10
altura = np.random.normal(170, 10, n) ## # Alturas com média 170 cm e desvio padrão 10
peso = np.random.normal(70, 10, n) ## # Pesos com média 70 kg e desvio padrão 10

dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})

dados['flag_fumante'] = dados['flag_fumante'].map({True: 'fumante', False: 'Não fumante'})

## Estilo
sea.set(style = 'ticks')

sea.lmplot(x = 'altura', y = 'peso', data = dados, hue = 'flag_fumante', palette= ['tab:blue', 'tab:orange'], height = 7)
## 'Hue' separa por cor -> Fumante ou não fumante
## 'Pallete' cores para cada grupo

plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre Altura e Peso de Fumantes e Não Fumantes')

## Remove as bordas
sea.despine()

plt.show()
