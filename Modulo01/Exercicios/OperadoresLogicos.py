# Operadores Lógicos

# Exemplos

# 8 > 4 # True
# 8 >= 7 # True
# 15 < 19 # True
# 8 >= 8 # Oito é maior ou igual - True
# 15 == 15 # Comparação - True
# 15 != 15 # Quinze é diferente de quinze - False

# Exercicios

# 1 - Verifique se um número está entre 10 E 20 (inclusive).

valor = 15

teste = valor >= 10 and valor <= 20

print(f'{teste}')

# 2 - Verifique se NÃO é múltiplo de 3.

mult = 10

verificandoMultiplo = mult % 3 != 0

print(f'{verificandoMultiplo}')

# 3 - Verifique se um aluno passa com média ≥ 7 OU com média ≥ 5 e frequência ≥ 75%.

mediaAluno = 8
frequenciaAluno = 60

verificaAprovacao = (mediaAluno >= 7) or (mediaAluno >= 5 and frequenciaAluno >= 75)

print(f'O aluno foi aprovado?: {verificaAprovacao}')
