# Aula 01 - Python para quem programa em C

### Intro
* Python é uma linguagem dinamicamente tipada. __Isto quer dizer que: variáveis não tem tipos, mas valores possuem tipos.__
* É possível introduzir anotação de tipos em Python. Não é algo que é checado pela linguagem, mas é algo bastante útil para fins de documentação. 
* É recomendado utilizar anotação de tipos em programas grandes. Entretanto, não é recomendado usar esse recurso em todas as variáveis do programa. O ideal é usar isso em declaração de funções
* Exemplo de definição de função (usando anotação de tipos):
```Python
def fatorial(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
```
