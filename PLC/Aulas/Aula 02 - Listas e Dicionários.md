# Aula 02 - Listas e Dicionários

### Intro
* Apanhado geral sobre conceitos envolvendo listas e dicionários em Python.

### Listas (Lists)
* São vetores dinâmicos. Sendo assim, são muito semelhantes ao "vector" de C++.
* Listas tem tipagem dinâmica. Ou seja, podem armazenar valores de tipos diferentes.
* É possível também trabalhar com anotações de tipo em Python mesmo com tipos compostos (listas, dicionários, sets, tuplas). No entanto, temos que fazer um import antes. Observe abaixo:
```Python
from typing import List

l1:List[int] = [1,2,3,4,5]

def getSumList(l: List[int]) -> int:
    sum = 0
    for x in l:
        sum = sum + x
    return sum
```
* Listas possuem alguns métodos bastante úteis que auxiliam na sua manipulação. São eles:
  * indexing -> O famoso operador ```[ind]```, que retorna um o valor presente na lista naquela posição. Lembrando que: 0 <= ind < len(lista)
  * .append(valor) -> Responsável por adicionar um elemento no final de uma lista.
  * pop() -> Responsável por excluir um elemento de uma lista baseado no seu índice. Caso, não passemos nenhum parâmetro dentro desse método, o último valor da lista é que será removido. __Vale ressaltar que esse método não só remove o valor como também o retorna.__
  * len(lista) -> Responsável por retornar o tamanho (qtd de elementos) de uma lista. __Essa aqui não é um método, mas sim uma função!!!__
  * Insert(ind, valor) -> Responsável por inserir um novo valor dentro de uma lista em um índice/posição específica.
* Existe mais um monte de métodos de listas para Python.

### Map, Filter e Fold em Listas de Python
* Assim como vimos em Haskell, podemos usar essas funções de alta ordem em Python, desde que em conjunto com lambdas.
* Observe alguns exemplos abaixo:
```Python
from functools import reduce

constantesFamosas: List[float] = [3.14, 1.41, 1.73, 2.24, 1.62, 0]

squared = list(map((lambda x: x*x), constantesFamosas)) 
evens = list(filter((lambda x: x % 2 == 0), constantesFamosas))
sumLista = reduce((lambda x, y: x + y), constantesFamosas, 0)
```

### Um pouco mais sobre Listas
* __Linhas em Python, funcionam como referencias. Ou seja, se definimos uma lista (por meio da criacao de uma variável) e depois a atribuimos a uma outra variável, as duas variáveis estão "apontando" para a mesma lista na memória. Tomar cuidado com isso!__
```Python
lista1 = [1,2,3]
lista2 = lista1 # Atribuição por referência 

lista2.append(4)
print(lista1) # [1,2,3,4]
print(lista2) # [1,2,3,4]
```
* __Para trabalhar com atribuição de cópia podemos fazer o seguinte:__
```Python
lista1 = [1,2,3]
lista2 = lista1[:] # Atribuição por cópia

lista2.append(4)
print(lista1) # [1,2,3]
print(lista2) # [1,2,3,4]
```
