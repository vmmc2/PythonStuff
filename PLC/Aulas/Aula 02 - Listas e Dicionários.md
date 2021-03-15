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
