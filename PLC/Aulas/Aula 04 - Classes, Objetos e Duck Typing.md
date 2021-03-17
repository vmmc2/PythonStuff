# Aula 04 - Classes, Objetos e Duck Typing

### Intro
* Em Python, além de termos objetos pré-definidos (como inteiros, strings, listas e dicionários), também podemos criar nossos próprios objetos.
* Para isso, devemos definir uma classe, que é como se fosse um novo tipo cujos valores serão os objetos.
* Exemplo de criação de uma classe para representar __horário:__
```Python
class Tempo:
    def __init__(self, h: int, m: int, s: int):
        self.segundo = s
        self.minuto = m
        self.hora = h
    def segundos(self):
        answer = 0
        answer = self.segundo + (self.minuto * 60) + (self.hora * 3600)
        return answer
        
# O parâmetro "self" referencia o próprio objeto que está sendo criado.
# Esse é uma parâmetro implícito, passado pelo próprio Python. E deve estar presente como primeiro parâmetro em todos os métodos definidos dentro de uma classe.


# A classe Tempo define um novo tipo.
t: Tempo = Tempo(21,42,24)
```
* __IMPORTANTE: Vale destacar que é possível criar atributos em objetos de forma dinâmica (em tempo de execução). Diferentemente do que acontece em C++/Java. No entanto, essa prática não é recomendada, pois pode ser surpreendente para algumas partes do programa.__

### Classes
* Classes definem novos tipos. Funcionam basicamente como um "blueprint" para novos tipos.
* Em geral, representam um conceito (por exemplo: o conceito de horário ou de uma estrutura de dados).
* Exemplos comuns: List, Dict, Turtle.
* __PyCharm e myPy verificam esses novos tipos criados, se forem indicados em variáveis ou funções.__
* O mesmo vale para novos tipos definidos pelo programador.

### Diferenças entre Classes e Objetos
* Objetos: Estado + Comportamento (Em outras palavras: Variáveis/Atributos + Funções/Métodos).
* Classes: Coleção de objetos (ou instâncias) com as mesmas características.

### Classes e a Keyword "Self"
* Todas as funções de uma classe (métodos) têm "self" como o primeiro parâmetro.
* __Esse parâmetro não é passado nas chamadas pelo programador!! Isso é feito debaixo dos panos pelo próprio Python.__
* __"self" indica que se está usando atributos e métodos do objeto.__
* Internamente a uma classe, "self" é sempre usado.

### Mais coisas importantes a respeito de Objetos em Python
* Se a gente tentar imprimir um objeto por meio da função ```print()``` sem antes definir algumas funções especiais, o resultado não será o esperado. Por exemplo:
```Python
agora: Tempo = Tempo(22,59,30)
print(agora)
<__main__.Tempo object at 0x7f8530e91d00>
# Ou seja, é impressa a localização do objeto na memória (endereço de memória) e o contexto em que a função print() foi chamada.
```
* O mesmo vale se nós tentarmos checar se dois objetos são iguais. Ou seja, comparador de igualdade ```==```. Devemos implementar uma outra função especial de Python para que isso funcione da forma adequada.
* Lembre que Objetos baseiam-se no modelo de semântica de referência.
```Python
agora: Tempo = Tempo(22,59,30)
passado: Tempo = Tempo(22,59,30)
passado == agora
False
# Mesmo que esses objetos tenham os mesmo valores em seus atributos internos, nós não definimos na classe Tempo nenhuma maneira de checar a igualdade entre dois objetos. Sendo assim, o que Python faz é verificar se esses objetos são na verdade o mesmo objeto (endereços iguais). Como isso não é verdade, o interpretador retorna False.
```
* Para resolver esse problema, é necessário implementar a nossa própria versão do método ```def __str__(self):```. Observe:
```Python
def __str__(self):
    return str(self.hora) + ":" + str(self.minuto) + ":" + str(self.segundo)
```
* Em Python, também existe o conceito de sobrecarga de construtores. Isto é construtores para um mesmo objeto mas que possuem uma quantidade de parâmetros diferentes e funcionam de formas distintas. 
* E se nós quisermos criar uma lista encadeada de tal forma que possamos iterar pelo seus elementos com um laço "for"? Para fazer isso, precisamos definir dois métodos dentro dessa classe: ```def __iter__(self):``` e ```def __next__(self):```
* Observe abaixo:
```Python
class LinkedListIterator:
    def __init__(self, e):
        self.elements = e
        self.current = e
    def __next__(self):
        if not self.current:
            raise StopIteration
        result = self.current
        self.current = self.current.next
        return result

class Node:
    def __init__(self, e):
        self.element = e
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.elements = None
        
    def __init__(self, e):
        self.elements = Node(e)
        
    def append(self, e):
        current = self.elements
        if current == None:
            self.elements = Node(e)
        else:
            while current.next != None:
                current = current.next
            current.next = Node(e)
        return
        
    def __iter__(self):
        return LinkedListIterator(self.elements)
```
