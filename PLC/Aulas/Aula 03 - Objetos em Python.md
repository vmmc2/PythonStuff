# Aula 03 - Objetos em Python

### Objetos
* __Em Python, objetos são valores que combinam estado e comportamento.__
  * O estado de um objeto é representado pelas variáveis existentes dentro de um objeto. (Também chamadas de atributos).
  * Já o comportamento de um objeto é representado por funções dentro de um objeto. (Também chamadas de métodos).
* __Em Python, temos que: números inteiros, strings, números de ponto flutuante (e outros) são objetos.__
* __Em outras palavras, na linguagem Python, todo tipo define um objeto.__

### Mais sobre Objetos
* Objetos são criados através de uma função especial chamada: construtor.
```Python
tmnt = Turtle() # Criando um objeto do tipo(classe) "Turtle".
```
* __Novamente, os objetos são valores. Ou seja, podem ser guardados em variáveis, passados como parâmetros, devolvidos por funções, etc...__
* __Suas variáveis internas (atributos) são manipuladas por meio de métodos.__
* __Como vimos na aula passada, objetos em Python utilizam semântica de referência. Ou seja, se eu crio um objeto por meio da atribuição de um construtor a uma variável ```a``` e depois de criado, eu atribuo essa variável ```a``` a uma outra variável ```b```, temos que ambos as variáveis estão apontando para o mesmo objeto na memória. (Funciona de forma semelhante a ponteiros em C/C++).__
