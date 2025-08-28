# Exercício – Cadastro de alunos

# 1 - Crie um programa que:
# Permita ao usuário cadastrar alunos com nome e idade.
# Guarde cada aluno em um dicionário.
# Armazene todos os dicionários em uma lista.
# Ao final, exiba a lista completa de alunos cadastrados.

#Exemplo

i = 1
alunosCadastrados = {}

while True:
    nomeAluno = input(f'Digite o nome do aluno que deseja cadastrar: ')
    alunosCadastrados[f"nome{i}"] = nomeAluno

    idadeAluno = input(f'Digite a idade do aluno que deseja cadastrar: ')
    alunosCadastrados[f"idade{i}"] = idadeAluno

    i = i + 1

    pergunta = input('Deseja continuar cadastrando? (Y/N) ')
    if pergunta == 'n' or pergunta == 'N':
        break

# Daqui para cima ↑↑↑ o código é 100% meu

# O GPT me ajudou a exibir o resultado de uma forma bonitinha e organizada no console.
# Ante eu estava usando a apenas um print(alunosCadastrados)
# Só usei o que ele sujeriu depois de entender o que o código dele faz.

for j in range (1, i):
    print(f'Aluno {j}: {alunosCadastrados[f'nome{j}']}')
    print(f'Idade do aluno {j}: {alunosCadastrados[f'idade{j}']}')
    print()