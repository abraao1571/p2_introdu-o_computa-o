chamados = {}
proximo_id = 100

while True:
    print("\nMenu:")
    print("1. Abrir Novo Chamado")
    print("2. Resolver Chamado")
    print("3. Relatório de Pendências")
    print("4. Sair do Sistema")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        descricao = input("Digite a descrição do chamado: ")
        chamados[proximo_id] = {"descricao": descricao, "status": "Aberto"}
        print(f"Chamado {proximo_id} aberto com sucesso!")
        proximo_id += 1
    elif opcao == 2:
        id_chamado = int(input("Digite o ID do chamado a ser resolvido: "))
        if id_chamado in chamados and chamados[id_chamado]["status"] == "Aberto":
            chamados[id_chamado]["status"] = "Resolvido"
            print(f"Chamado {id_chamado} resolvido com sucesso!")
        else:
            print("Chamado não encontrado ou já resolvido.")
    elif opcao == 3:
        print("\nRelatório de Pendências:")
        for id_chamado, info in chamados.items():
            if info["status"] == "Aberto":
                print(f"ID: {id_chamado}, Descrição: {info['descricao']}, Status: {info['status']}")
    elif opcao == 4:
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida. Tente novamente.")