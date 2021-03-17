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


# A classe Tempo define um novo tipo.
t: Tempo = Tempo(21,42,24)
```
* __IMPORTANTE: Vale destacar que é possível criar atributos em objetos de forma dinâmica (em tempo de execução). Diferentemente do que acontece em C++/Java.__
