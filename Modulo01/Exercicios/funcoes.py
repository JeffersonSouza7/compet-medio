# Exercícios:

# 1 - Função soma_lista(lista) → soma.

def soma_lista(lista):

    soma = 0
    for num in lista:
        soma = soma + num
    return soma
 
lista = [1, 2, 3]
soma = soma_lista(lista)
print(soma)

# 2 - Função eh_par(n) → True/False.

def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

pergunta = int(input('Digite um numero qualquer: '))

resultado = eh_par(pergunta)
print(f'O resultado é: {resultado}')

# 3 - Função boletim(n1, n2) → média e situação (≥7 aprovado, 5–6.9 recuperação, <5 reprovado).

def boletim(n1, n2):

    media = (n1 + n2) / 2
    
    if media >= 7:
        situacao = 'Aluno aprovado'
    elif media >= 5 and media <= 6.9:
        situacao = 'Aluno em recuperação'
    else:
        situacao = 'Aluno reprovado'

    print(f'A media das notas foi de: {media:.2f} e a sua situação é: {situacao}')


# Perguntando as notas
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))

# Chamando a função passando nota1 e nota2 como paramêtros
boletim(nota1, nota2)
