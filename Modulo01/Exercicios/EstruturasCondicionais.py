#Estrutura condicional

# 1 - Classifique IMC
# <18.5 = magreza
# 18.5 - 24.9 = normal
# 25 - 29.9 = sobrepeso
# >= 30 = obesidade

peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print(f'Seu imc é de: {round(IMC, 2)}, e você está muito magro')
elif IMC > 18.5 and IMC <= 24.9:
    print(f'Seu imc é de: {round(IMC, 2)}, e você está no peso normal')
elif IMC >= 25 and IMC <= 29.9:
    print(f'Seu imc é de: {round(IMC, 2)}, e você está com sobrepeso')
elif IMC >= 30:
    print(f'Seu imc é de: {round(IMC, 2)}, e você está com obesidade')


# 2 - Diga se um número é par, ímpar ou zero.

numero = int(input('Digite um número qualquer: '))

if numero == 0:
  print(f'Você digitou o numero {numero}!')
elif numero % 2 != 0:
  print(f'O numero {numero} é impar!')
elif numero % 2 == 0:
  print(f'O numero {numero} é par!')