# Aula 11 Bootcamp Python - Jornada de Dados
# Programação Orientada a Objetos (POO) em Python

## Introdução

A **Programação Orientada a Objetos (POO)** é um paradigma de programação que organiza o código em torno de **objetos**, que representam entidades do mundo real. Esse modelo facilita a reutilização, modularidade e manutenção do código.

Em Python, a POO é implementada principalmente por meio de **classes** e **objetos**.

## Classes e Objetos em Python

### O que é uma Classe?
Uma **classe** é um modelo ou estrutura que define um conjunto de atributos e métodos para criar objetos.

### O que é um Objeto?
Um **objeto** é uma instância de uma classe, ou seja, um elemento criado com base no modelo definido pela classe.

### Exemplo de Classe e Objeto

```python
# Definição de uma classe
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo
        self.modelo = modelo  # Atributo
        self.ano = ano  # Atributo

    def descrever(self):
        return f"{self.marca} {self.modelo}, Ano: {self.ano}"

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022)

# Chamando um método
print(meu_carro.descrever())
```

### Explicação do Código
1. Criamos a classe `Carro` com um **método construtor** `__init__` para inicializar os atributos `marca`, `modelo` e `ano`.
2. Definimos o método `descrever`, que retorna uma descrição do carro.
3. Criamos um **objeto** `meu_carro` da classe `Carro` e utilizamos o método `descrever` para exibir suas informações.

## Benefícios da POO
✅ **Reutilização de Código** – Classes podem ser reutilizadas para criar múltiplos objetos.\
✅ **Modularidade** – O código é organizado em componentes independentes.\
✅ **Facilidade de Manutenção** – Alterações no código afetam apenas partes específicas.\
✅ **Encapsulamento** – Os detalhes internos do objeto são protegidos e acessíveis apenas por métodos específicos.

## Conclusão

A Programação Orientada a Objetos permite organizar o código de forma estruturada e reutilizável. Python oferece suporte completo a esse paradigma, tornando-o ideal para desenvolvimento de aplicações escaláveis e fáceis de manter.

Caso queira explorar mais sobre POO em Python, consulte a [documentação oficial](https://docs.python.org/pt-br/3/tutorial/classes.html).
