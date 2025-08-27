# Exercícios:

# 1 - Some os números de 1 a 100.

soma = 0
for i in range (1, 101):
    soma = soma + i

print(f'A soma de todos os numeros de 1 a 100 é igual a: {soma}')

# 2 - Leia números até digitar 0 e mostre a quantidade lida.

contador = 0

while True:
    numeroLido = int(input('Digite um numero qualquer (0 para sair): '))
    if numeroLido == 0:
        break
    contador = contador + 1
    

print(f'Você digitou {contador} numeros até digitar o numero 0')

# 3 - Imprima a tabuada de um número de 1 a 10.

tabuadaDe = int(input('Digite o numero do qual você quer ver a tabuada: '))
ateQuanto = int(input('Até que numero vamos multiplicar? '))

for j in range (1, (ateQuanto + 1)):
    print(f'{tabuadaDe} X {j} = {tabuadaDe * j}')