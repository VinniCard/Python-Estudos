#%%

import pandas as pd
import numpy as np


## Criando um array
arrl = np.array([10,21,32,43,15,67,57,89])

## Vetor
arrl.shape ## Arrl.shape -> (8,)

## Arrays do NumPy são mais eficientes do que as listas do Python para armazenar e manipular grandes quantidades de dados.

## -----------------------------------------------------------------------------------------------------------------------------------

## Indexação em Arrays NumpPy

print(arrl) 

## Imprimindo um elemento específico no array

arrl[4] ## arrl[4] -> 15

## Indexação 

arrl[1:4] ## arrl[1:4] -> array([21, 32, 43])

arrl[1:4+1]

## Cria uma lista de índices

indices = [1,2,5,6]

arrl[indices] ## -> array([21, 32, 67, 57])

## Cria uma máscara booleana para os elementos pares

mask = (arrl % 2 == 0) ## -> array([ True, False,  True, False, False, False, False, False])
mask

arrl[mask] ## -> array([10, 32])

## Alterando um elemento do array

arrl[0] = 100
print(arrl) ## -> [100  21  32  43  15  67  57  89]

## Não é possivel incluir elemento de outro tipo

##--------------------------------------------------------------------------------------------------------------------------------------

## Funções NumPy

arr2 = np.array([1,2,3,4,5])

## Digite arr2. e pressione a tecla Tab para visualizar métodos disponiveis em objetos Numpy

## Função arange para criar um array contendo uma progressão aritimética a partir de um intervalo - start, stop, step

arr3 = np.arange(0, 50, 5) ## -> [100  21  32  43  15  67  57  89]
print(arr3)

## Formato do array

np.shape(arr3) ## -> (10,)


## Verificando o tipo do objeto

type(arr3) ## -> numpy.ndarray

## Criar um array preenchido com zeros

arr4 = np.zeros(10) ## -> numpy.ndarray
print(arr4)

## Retorna 1 nas posições em diagonal e 0 no restante, matriz diagonal

arr5 = np.eye(3) ## -> [[1. 0. 0.]
                 ## -> [0. 1. 0.]
                 ## -> [0. 0. 1.]]
print(arr5)


## Criar uma matriz diagonal

arr6 = np.diag(np.array([1,2,3,4]))
print(arr6)

## Array de valores booleanos

arr7 = np.array([True, False, False, True]) ## -> [ True False False  True]
print(arr7)

## Array de strings

arr8 = np.array(['Pyhton', 'R', 'SQL', 'BI']) ## -> ['Pyhton' 'R' 'SQL' 'BI']
print(arr8)

## --------------------------------------------------------------------------------------------------------------------------------------

## Manipulando Matrizes

## Criando uma Matriz

arr9 = np.array([[1,2,3], [4,5,6]]) ## _>[[1 2 3]
                                    ## ->[4 5 6]]
print(arr9)

## Shape

print(arr9.shape) ## -> (2, 3)

## Crinando uma matriz 2x3 apenas com números "1"

arr10 = np.ones((2,3)) ## 2 linhas e 3 colunas

## Listas de Listas

lista = [[12,81,22], [0,34,59], [21,48,94]]

## A função Matrix cria uma matriz a partir de uma lista de listas

arr11 = np.matrix(lista)

type(arr11) ## -> numpy.matrix

## Array melhor utilizado para armazenar dados, analise de dados, ciência de dados e machine learning. (fatiar, indexar, armazenar, separar)
## Matriz melhor para se utilizar se for necessario aplicar operações matematicas

## Formato da matriz

np.shape(arr11) ## -> (3, 3)

## Tamanho da matriz

arr11.size ## -> 9

## Indexação da matriz
## Sempre Linha primeiro e colunas depois, lembrando que o index começa no 0 no Pyhton

arr11[2,1]  ## -> 48

arr11[0:2, 2] ## -> 22 e 59

arr11[1, ] ## -> 0, 34, 59

## Alterando um elemento da matriz

arr11[1,0] = 100

## Mudar o tipo do dado

x = np.array([1,2], dtype = np.float64) # Forçando um tipo de dado em particular

arr12 = np.array([[24,76,92,14], [47,35,89, 2]], dtype = float)


## Itemsize, tamanho em bytes em cada elemento do array. Representando o número de bytes necessários para armazenar cada valor do array numpy

arr12.itemsize ## -> 8

arr12.nbytes ## -> 64

arr12.ndim ## -> 2

## -------------------------------------------------------------------------------------------------------------------------------

## Análise estatística básica

arr14 = np.array([15,23,63,94,75])

## Média
np.mean(arr14) ## -> 54.0

## Desvio padrão -> Avaliar a consistência dos dados e avaliar a variabilidade dos dados em torno da média

np.std(arr14) ## -> 30.34468652004828

## Variância -> Número que indica a dispersão dos dados

np.var(arr14) ## -> 920.8

## --------------------------------------------------------------------------------------------------------------------------------

## Operações Matemáticas com Arrays Numpy

arr15 = np.arange(1,10) ## -> array([1, 2, 3, 4, 5, 6, 7, 8, 9])

## Soma
np.sum(arr15) ## -> 45

## Soma acumulada

np.cumsum(arr15) ## -> array([ 1,  3,  6, 10, 15, 21, 28, 36, 45], dtype=int32)

## Soma dos arrays

arr16 = np.array([3,2,1])
arr17 = np.array([1,2,3])

arr18 = np.add(arr16, arr17) ## -> [4 4 4]
print(arr18)

## Multiplicação de Matrises -> Número de colunas da primeira matriz, tem que ser igual ao número de linhas da segunda matriz

arr19 = np.array([[1,2], [3,4]])
arr20 = np.array([[5,6],[0,7]])

arr21 = np.dot(arr19, arr20)

## -----------------------------------------------------------------------------------------------------------------------------------

## Slicing (Fatiamento) de Arrays Numpy

arr22 = np.diag(np.arange(3))

## Coluna e linha
arr22[1,1] ## -> 1

## Linha
arr22[1] ## -> array([0,1,0])

## Coluna
arr22[:,2] ## -> array([0,0,2])

arr23 = np.arange(10)

## Start:End:Step
arr23[2:9:3] ## -> array([2,5,8])

a = np.array([1,2,3,4])
b = np.array([4,2,2,4])

## Comparação Item a Item

a == b ## -> array([False, True, False, True])

## Comparação global

np.array_equal(a,b)

arr23.min() ## -> 0

arr23.max() ## -> 9

## Somando um valor a cada elementp do array

np.array([1,2,3]) + 1.5 ## -> array([2.5, 3.5, 4.5])

## Método around
arr24 = np.array([1.2,1.5,1.6,2.5,3.5,4.5])

arr25 = np.around(arr24) ## -> [1. 2. 2. 2. 4. 4.]
print(arr25)

##

arr26 = np.array([[1,2,3,4], [5,6,7,8]])

## Método flatten()

arr27 = arr26.flatten() ## -> [1 2 3 4 5 6 7 8]
print(arr27)

## Repetindo os elementos de um array

arr28 = ([1,2,3])

np.repeat(arr28, 3) ## -> array([1, 1, 1, 2, 2, 2, 3, 3, 3])

## Repetindo os elementos de um array

np.tile(arr28, 3) ## -> array([1, 2, 3, 1, 2, 3, 1, 2, 3])

## Criando a copia de um array

arr29 = np.array([5,6])

arr30 = np.copy(arr29)