# Aula 01 - Python para quem programa em C

### Intro
* Python é uma linguagem dinamicamente tipada. __Isto quer dizer que: variáveis não tem tipos, mas valores possuem tipos.__
* É possível introduzir anotação de tipos em Python. Não é algo que é checado pela linguagem, mas é algo bastante útil para fins de documentação. 
* É recomendado utilizar anotação de tipos em programas grandes. Entretanto, não é recomendado usar esse recurso em todas as variáveis do programa. O ideal é usar isso em declaração de funções
* Exemplo de definição de função (usando anotação de tipos):
```Python
def fatorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
```

### Tipos
* Python possui ```int```, ```float```, ```str```, ```bool```.
* Entretanto, Python não possui um tipo ```char```.
* Falando de tipos ```bool```, temos que em linguagens dinâmicas, como Python, existe uma maior flexibilidade para lidar com valores de tal tipo. __No caso particular de Python, temos que o valor ```True``` é syntactic sugar para o valor ```1```. De maneira análoga, o valor ```False``` é syntactic sugar para o valor ```0```.__
* Observe o exemplo abaixo:
```Python
True + 1 # == 2
False - 3 # == -3
```
* Reciprocamente, qualquer valor numérico diferente de 0 representa o valor booleano ```True```. Por outro lado, 0 representa ```False```.
