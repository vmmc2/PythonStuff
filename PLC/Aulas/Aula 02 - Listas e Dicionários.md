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
  * .append() -> Responsável por adicionar um elemento no final de uma lista.
  * pop() -> Responsável por excluir um elemento de uma lista baseado no seu índice. Caso, não passemos nenhum parâmetro dentro desse método, o último valor da lista é que será removido. __Vale ressaltar que esse método não só remove o valor como também o retorna.__
  * len() -> Responsável por retornar o tamanho (qtd de elementos) de uma lista.
* Existe mais um monte de métodos de listas para Python.
