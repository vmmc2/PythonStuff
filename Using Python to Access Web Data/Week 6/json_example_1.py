# JSON Parsing Example 1
import json # necessario para fazer o parsing do json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456" 
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data) # Essa funcao do modulo json eh responsavel por pegar uma string que representa um json
# e transformar ele em um objeto json. Nesse caso, perceba a semelhanca entre um objeto json e um dicionario em python.
# Eles sao iguais sintaticamente falando. Devido a isso, o objeto JSON eh convertido em dicionario de python.
# E com isso, podemos acessar cada campo dentro do json como se estivessemos trabalhando com um dicionario de python.

print('Name:', info['name'])
print('Hide:', info['email']['hide'])
