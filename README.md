# ANOTAÇÕES DE FUNDAMENTOS DA PROGRAMAÇÃO

## Tipos de dados em python
1. string 
2. number int
3. number float 
4. boolean

## Operadores matemáticos - básicos

+ -> adição
- -> subtração
* -> multiplicação 
/ - > divisao 

## Operadores Logicos 

and -> e -> Se duas condições forem verdadeiras, o resultado é verdadeiro
or -> ou -> Se pelomenos uma condição for verdadeira, o resultado é verdadeiro.
not ->

## Métodos em python

1. print() -> Exibe informações no terminal.
2. input() -> Capturar uma informação no terminal
3. lower() -> Converte toda a string em minúscula.
4. upper() -> Converte toda a string em maiúscula.
5. isdigit() - Verifica se o valor contém número.

## Format em python

# Estrutura condicional
 ``if (se)`` -> Verifica se uma informação é true. Se for ele executa o código 
 ``elif (senão se)`` -> É usado para testar várias condições. Ele só executa o código
 ``else (senão)`` ->Executa o código se a condiçõo if for false 

# Laços de repetição
É um recurso de programação que permite executar um comando várias vezes. Também são chamados de
Loop,Laços de repetição ou iteração.
`FOR` -> Utilizamos quando sabemos quantas vezes queremos repetir algo.
Sintax:
for variavel in range(inicio,fim):
    comandos
[range()] -> Método que aceita geração de números.
[inicio] -> É inclusivo. É o primeiro número a ser usado.
[fim] -> É exclusivo

## Escopo das Variáveis
´`´Escopo Global` -> a variável pode ser acessadapor todo mundo

## Variaçoes das variáveis
Variável em memória -> é delarada quando voce não pretende utilizar essa variavel em outros cenarios.
Variável contadora -> é utilizada para uma logica onde a repetiçao ira ser alterada 

`WHILE` -> E utilizado quando não sabemos quantas vezes o programa vai repetir. Ele repete quanto uma condição for verdadeira.
Sintaxe:
while condicao:
      comandos 

## Conversão de Tipos em python
1.int() -> A gente vai incluir qualquer variável/dado que queremos converter para número inteiro.
2.float() -> A gente vai incluir qualquer variável/dado que queremos converter para número decimal.
3.str() -> A gente vai incluir qualquer variável/dado que queremos converter para texto.



 ## Boas Práticas
 1. Qualquer variavel em py utiliza o padrao de case snake_case ou recentemente o cammelCase.
 2. Se voce observar alguma estrutura tipo nome () 90% de chance de ser uma função.
 3. Python não tem constante porém utilizamos o padrão UPPERCASE , para simular que aquela variável não pode ser alterada.



 ## Funções em Python

 `def` -> Define que uma função será declarada;

 `propriedade` -> Variável em memória que irá receber um argumento;

 `argumento` -> [Valor] que ira preeencher o espaço da propriedade;

 ## Estruturas de Dados
 `list ou lista` -> Armazena valores avulsos e podem ser heterogenea ou 
 homogenea. Ou seja, pode guardar valores de um mesmo tipo ou de diferentes tipos.
 Ex: list= [] // lista vazia
 list= ["Gabriel",18,1.70]

 `dict ou dicionário` -> Armazena conjuntos de valores (chave:valor).As chaves 
 e valores podem ser heterogenea ou homogenea

 1. Para obter o valor de um conjunto em dict,voce acessa pela chave.
 Ex: dados_usuario ={"nome: "Gabriel", "cpf": 145678908-66 , "idade": 18}
 dados_usuario["nome"] => Devolve o valor,que é "Gabriel".