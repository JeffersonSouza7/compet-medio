# Exemplos

# 'abs()' retorna o valor absoluto de um número
# 'max()' retorna o valor máximo de uma sequência
# 'min()' retorna o valor minímo

# Exercicios

# 1 - Peça ao usuário para digitar 3 números inteiros e:
# Use a função max() para mostrar o maior número.
# Use a função min() para mostrar o menor número.
# Use a função sum() para mostrar a soma deles.

numero1 = int(input('Digite o 1º numero: '))
numero2 = int(input('Digite o 2º numero: '))
numero3 = int(input('Digite o 3º numero: '))

numeros = [numero1, numero2, numero3]

print(f'O maior numero digitado foi: {max(numeros)}')
print(f'O menor numero digitado foi: {min(numeros)}')
print(f'A soma dos 3 numero e igual a: {sum(numeros)}')

# 2 - Peça ao usuário para digitar uma palavra e:
# Mostre a palavra em maiúsculas (função upper()).
# Mostre a palavra em minúsculas (função lower()).
# Mostre quantas letras a palavra tem (função len()).

palavra = input('Digite uma palavra qualquer: ')

print(f'A palavra em maiusculas é:', palavra.upper())
print(f'A palavra em minusculas é:', palavra.lower())
print(f'A palavra tem um total de:', len(palavra),'letras')



# 3 - Leia 3 números em uma lista e exiba max, min e sum.

listaNumeros = [3, 5, 7]

print('O maior, o menor e a soma de todos os 3 numeros são respectivamente:', max(listaNumeros),',', min(listaNumeros), 'e', sum(listaNumeros))

# 4 - Arredonde 7/3 com 2 casas.

divisao = (7/3)

print(round(divisao, 2))

# 5 - Transforme "42" em int e "3.5" em float.

valorInt = "42"
valorFloat = "3.5"

print(f'A variavel "valorInt" agora é do tipo ', type(int(valorInt)))
print(f'A variavel "valorFloat" agora é do tipo ', type(float(valorFloat)))