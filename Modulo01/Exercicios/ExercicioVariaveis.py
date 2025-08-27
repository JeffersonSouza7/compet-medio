# Exercicios variaveis

# 1 - Crie umn programa que solocite ao usuario seu nome, idade e altura.
# Guarde essas informações em variaveis e as exiba no console na forma de
# uma mensagem.

nomePessoa = input('Qual o seu nome? ')
idadePessoa = input('Qual a sua idade? ')
alturaPessoa = input('Qual a sua altura? ')

print(f'Seu nome é {nomePessoa}, você tem {idadePessoa} anos e sua altura é {alturaPessoa}')


# 2 - Defina uma constante PI com o valor 3.14159. Solicite ao usuario o raio
# de um circulo, e depois calculo e exiba a area do circulo

PI = 3.14159
raio = float(input('Digite o raio da circunferência: '))
areaCirculo = (PI * (raio * raio))

print(f'A area do circulo de raio {raio} é igual a: {areaCirculo:.2f}m²') #':.2F' 
# O ':.2f' indica que o número deve ser exibido como um float (f) com exatamente 2 casas decimais (.2).


# 3 - Crie variaveis nome(str), idade (int) e altura (float). Use 'type()' para exibir os tipos.

nome = 'Jeff'
idade = 27
altura = 1.73

print(f'Tipo de dado da variavel nome: {type(nome)}')
print(f'Tipo de dado da variavel idade: {type(idade)}')
print(f'Tipo de dado da variavel altura: {type(altura)}')

# 4 - Defina a constante TAXA_JUROS = 0.02 e calcule o juros de R$1000.

TAXA_JUROS = 0.02
valorEmprestimo = 1000
calculoJuros = valorEmprestimo * TAXA_JUROS

print(f'O valor do juros do emprestimo de R${valorEmprestimo} a uma taxa de juros de {TAXA_JUROS} é igual a: R${calculoJuros:.2f}')