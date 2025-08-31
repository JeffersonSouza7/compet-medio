import os

alunosMatriculados = []

def cadastrar():
  
    #Limpatela ao entrar na função
    os.system("cls")

    #Contador do numero das matriculas
    numeroMatricula = 1
    
    while True:

        print("*** Bem vindo a Area de Cadastro ***\n")

        print('1 - Cadastrar novo aluno')
        print('2 - Sair\n')

        perguntaInicial = int(input('Escolha uma opção: '))


        if perguntaInicial == 2:
          return

        elif perguntaInicial == 1:
          
          nomeAluno = str(input("Digite o nome do aluno que deseja cadastrar: "))
          matriculaAluno = numeroMatricula

          nota1 = float(input("Digite a primeira nota: "))
          nota2 = float(input("Digite a segunda nota: "))

          MEDIA_NOTAS = (nota1 + nota2) / 2

          if MEDIA_NOTAS >= 7:
            situacao = "Aluno aprovado"
          elif MEDIA_NOTAS > 5 and MEDIA_NOTAS < 6.9:
            situacao = "Aluno em recuperação"
          elif MEDIA_NOTAS < 5:
            situacao = "Aluno reprovado"

          novoAluno = {"Nome: ": nomeAluno, "Nº matricula: ": matriculaAluno, "Primeira Nota: ": nota1, "Segunda Nota: ": nota2, "Media das Notas: ": MEDIA_NOTAS, "Situação do aluno: ": situacao}

          alunosMatriculados.append(novoAluno)

          numeroMatricula = numeroMatricula + 1

        while True:
          perguntaFinal = input('Deseja continuar cadastrando? (Y/N): ').lower()
          if perguntaFinal == 'y':
              os.system("cls")
              break
          elif perguntaFinal == 'n':
              os.system("cls")
              return
          else:
            print('Digite apenas y ou n')

def alterar():

  os.system("cls")

  #Se não tiver nenhum aluno matriculado
  if not alunosMatriculados:
    print("Nenhum aluno matriculado")
    input("\nPressione ENTER para continuar...")
    return

  #Caso tenha aluno(s) matriculados
  print("*** Central de Alteração Cadastral ***\n")

  #Exibindo os nomes e matriculas
  for aluno in alunosMatriculados:
    print(f"Nome: {aluno["Nome: "]}  - Matricula: {aluno["Nº matricula: "]}")

  perguntaAlterar = int(input('Qual o Nº da matricula do aluno você deseja alterar o cadastro?: '))
  print("\n")
  
  # Verificando se o aluno existe no cadastro
  for aluno in alunosMatriculados:
    if aluno["Nº matricula: "] == perguntaAlterar:
      print(f"Aluno encontrado! Nome:", aluno["Nome: "],"\n")
      print("O que você deseja alterar?\n")
      print('1 - Nome do Aluno')
      print('2 - Nº da matricula')
      print('3 - Primeira Nota')
      print('4 - Segunda Nota')
      print('5 - Visualizar Media e Situação')
      print('6 - Sair \n')

      alterarDados = int(input('O que você deseja alterar?: '))

      # Alterando o nome do aluno
      if alterarDados == 1:
        novo_NomeAluno = input(f"Digite o novo nome do aluno {aluno["Nome: "]}: ")
        aluno["Nome: "] = novo_NomeAluno
        print(f'Nome alterado para: {novo_NomeAluno}')
        
      
      #Alterando o numero da matricula
      elif alterarDados == 2:
        novo_NumeroMatricula = input(f"Digite o novo numero de matricula do aluno {aluno["Nome: "]}: ")
        aluno["Nº matricula: "] = novo_NumeroMatricula
        print(f'Nº alterado para: {novo_NumeroMatricula}')
        

      #Alterando a primeira nota
      elif alterarDados == 3:
        nova_PrimeiraNota = float(input(f'Digite a nova primeira nota do aluno {aluno["Nome: "]}: '))
        aluno["Primeira Nota: "] = nova_PrimeiraNota
        print(f'Primeira nota alterada para: {nova_PrimeiraNota}')

        nova_MediaNotas = (aluno["Primeira Nota: "] + aluno["Segunda Nota: "]) / 2
        aluno["Media das Notas: "] = nova_MediaNotas

        if nova_MediaNotas > 7:
          aluno["Situação do aluno: "] = "Aluno aprovado"
        elif nova_MediaNotas > 5 and nova_MediaNotas < 6.9:
          aluno["Situação do aluno: "] = "Aluno em recuperação"
        elif nova_MediaNotas < 5:
          aluno["Situação do aluno: "] = "Aluno reprovado"

      
      #Alterando a segunda nota
      elif alterarDados == 4:
        nova_SegundaNota = float(input(f'Digite a nova segunda nota do aluno {aluno["Nome: "]}: '))
        aluno["Segunda Nota: "] = nova_SegundaNota
        print(f'Segunda nota alterada para: {nova_SegundaNota}')

        nova_MediaNotas = (aluno["Primeira Nota: "] + aluno["Segunda Nota: "]) / 2
        aluno["Media das Notas: "] = nova_MediaNotas

        if nova_MediaNotas >= 7:
          aluno["Situação do aluno: "] = "Aluno aprovado"
        elif nova_MediaNotas >= 5 and nova_MediaNotas >= 6.9:
          aluno["Situação do aluno: "] = "Aluno em recuperação"
        elif nova_MediaNotas < 5:
          aluno["Situação do aluno: "] = "Aluno reprovado"
        
       
      
      #Visualizando a media e a situação atual
      elif alterarDados == 5:
        print(f'A media atual do aluno {aluno["Nome: "]} é: {aluno["Media das Notas: "]}\n')
        print(f'A situação atual do aluno {aluno["Nome: "]} é: {aluno["Situação do aluno: "]}')

        input("\nPressione ENTER para continuar...")
        os.system("cls")

      elif alterarDados == 6:
        return
      
      else:
        print('Erro, digite um valor válido!')

def excluir():

  print("*** Central de Exclusão Cadastral ***\n")

  if not alunosMatriculados:
    print("Nenhum aluno matriculado")
    input("\nPressione ENTER para continuar...")
    return

  #Exibindo os nomes e matriculas
  for aluno in alunosMatriculados:
    print(f"Nome: {aluno["Nome: "]}  - Matricula: {aluno["Nº matricula: "]}")
  
  perguntaExcluir = int(input('Qual o Nº da matricula do aluno você deseja excluir o cadastro?: '))

  #Procurando e excluindo o aluno do cadastro
  for aluno in alunosMatriculados:

    if aluno["Nº matricula: "] == perguntaExcluir:
      alunosMatriculados.remove(aluno)
      print(f'Cadastro do aluno {aluno["Nome: "]} excluido com sucesso!')
    else:
      print(f'Matricula não encontrada.')
      break



def listar():
  os.system("cls")
  print('*** Lista de Alunos Matriculados ***\n')
  
  #Se a lista estiver vazia
  if not alunosMatriculados:
    print("Nenhum aluno matriculado")

  else:
  #Caso tenha alunos matriculados
    for aluno in alunosMatriculados:
      for chave, valor in aluno.items():
          print(f"{chave}{valor}")
      print("-" * 40)

  input("\nPressione ENTER para continuar...")
  os.system("cls")
# Inicio do programa

while True:

  print('*** Bem vindo ao portal EduSimples ***\n')
  print('Escolha uma opção: ')

  print('1 - Cadastrar\n2 - Alterar\n3 - Excluir\n4 - Listar alunos matriculados\n5 - Sair do Sistema\n')

  try:
    opcao = int(input('Digite a sua opção: '))
  
    if opcao == 1:
      cadastrar()
    elif opcao == 2:
      alterar()
    elif opcao == 3:
      excluir()
    elif opcao == 4:
      listar()
    elif opcao == 5:
      break

  except ValueError:
    print("Digite uma opção válida!")

print('Sistema finalizado com sucesso!!!!')