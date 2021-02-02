# POO: programação orientada a objetos

Este diretório contém assuntos básicos e intermediários sobre POO em python.

## Convenções de nomes

Como você viu na aula anterior, usamos certas convenções para nomes de variáveis, funções, classes e assim por diante. Essas convenções tem um nome que podemos usar para nos referir ao modo como estamos nomeando determinados objetos em nosso programa: PascalCase, camelCase e snake_case.

**PascalCase** - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a convenção utilizada para classes em Python;

**camelCase** - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra sempre será minúscula e o restante das palavras deverá iniciar com letra maiúscula. Como em: minhaFuncao, funcaoDeSoma, etc... Essa conversão não é usada em Python (apesar de eu confundir as duas e às vezes acabar chamando camelCase de PascalCase ou vice-versa, mas agora você sabe a diferença);

**snake_case** - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.

## Tipos de relação entre classes

* associação - um objeto usa outro objeto

* agregação - um objeto tem outro(s) objeto(s) como parte de sí

* composição - um objeto é dono de outro(s) objeto(s)

* herança - um objeto é/herda outro objeto

## Classes abstratas

São classes genéricas que não se deseja instanciar.

Pode ter métodos concretos e métodos abstratos. Os métodos concretos funcionam normal como métodos simples. Já o abstrato não possui corpo, cria-se o método, o código não é escrito e então é dito que ele é abstrato para que outras classes filhas herdem e sejam obrigadas a criá-lo dentro de sí.

Uma classe abstrata força que outras classes que a herdaram faça determinada coisas, criem determinados métodos obrigatoriamente.

## Metaclasses

São classes que criam classe.
