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
