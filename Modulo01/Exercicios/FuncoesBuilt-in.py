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




