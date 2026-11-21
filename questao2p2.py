def cadastrar_aluno(fila):
    nome = input("digite o nome do aluno: ")
    fila.append(nome)
def cadastrar_aluno_prioridade(fila):
    nome = input("Digite o nome do aluno com prioridade: ")
    fila.insert(0, nome)
def remover_aluno(fila):
    nome = input("Digite o nome do aluno a ser removido: ")
    if nome in fila:
        fila.remove(nome)
        print(f"Aluno {nome} removido da fila.")
    else:
        print(f"Aluno {nome} não encontrado na fila.")
def consultar_posicao(fila):
    nome = input("Digite o nome do aluno para consultar a posição: ")
    if nome in fila:
        posicao = fila.index(nome) + 1
        print(f"Aluno {nome} está na posição {posicao} da fila.")
    else:
        print(f"Aluno {nome} não encontrado na fila.")

def gerenciar_fila(fila):
    while True:
        print("\nMenu:")
        print("1. Cadastrar aluno normal")
        print("2. Cadastrar aluno prioridade")
        print("3. Remover aluno")
        print("4. Consultar posicao")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_aluno(fila)
            print("Aluno cadastrado com sucesso.")
            print("Fila atual:", fila)
        elif opcao == "2":
            cadastrar_aluno_prioridade(fila)
            print("Aluno com prioridade cadastrado com sucesso.")
            print("Fila atual:", fila)
        elif opcao == "3":
            remover_aluno(fila)
            print("Fila atual:", fila)
        elif opcao == "4":
            consultar_posicao(fila)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

alunos = []
gerenciar_fila(alunos)