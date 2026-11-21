def contabilizar_acessos(tipo):
  contagem = {}

  for passe in tipo:
    if passe == "Erro_leitura":
      continue

    if passe in contagem:
      contagem[passe] += 1
    else:
      contagem[passe] = 1

  return contagem

ru = []
while True:
    print("\nTipo do Usuário:")
    print("1. Normal")
    print("2. Bolsista")
    print("3. Professor")
    print("4. Pós_Graduação")
    print("5. Erro de Leitura")
    print("6. Cartão Bloqueado")
    print("7. Encerrar Acesso")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        ru.append("Normal")
        print("Acesso permitido. Bem-vindo ao RU!")
    elif opcao == 2:
        ru.append("Bolsista")
        print("Acesso permitido. Bem-vindo ao RU!")
    elif opcao == 3:
        ru.append("Professor")
        print("Acesso permitido. Bem-vindo ao RU!")
    elif opcao == 4:
        ru.append("Pós_Graduação")
        print("Acesso permitido. Bem-vindo ao RU!")
    elif opcao == 5:
        ru.append("Erro_leitura")
        print("Erro de leitura. Tente novamente.")
    elif opcao == 6:
        ru.append("Cartao_bloqueado")
        print("Cartão bloqueado. Acesso negado.")
        if ru.count("Cartao_bloqueado") >= 3:
            print("ALERTA: Tentativa de fraude identificada. Sistema travado por motivos de segurança")
            print(ru)
            print("Contagem de acessos:", contabilizar_acessos(ru))
            break
    elif opcao == 7:
        print("Encerrando acesso")
        print(ru)
        print("Contagem de acessos:", contabilizar_acessos(ru))
        break