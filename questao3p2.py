def verificar(matriz, limite):
    alerta = []
    for bloco in range(len(matriz)):
        for dia in range(len(matriz[bloco])):
            if matriz[bloco][dia] >= limite:
                alerta.append((bloco, dia))
    return alerta

consumo = []
for bloco in range(4):
    for dia in range(5):
        valor = int(input(f"Digite o consumo do bloco {bloco+1} no dia {dia+1}: "))
        if len(consumo) <= bloco:
            consumo.append([])
        consumo[bloco].append(valor)

print("Consumo registrado:")
for bloco in consumo:
    print(bloco)

limite = int(input("Digite o limite de consumo: "))

print("verificando")
alertas = verificar(consumo, limite)
print("Blocos e dias com consumo acima do limite:")
for bloco, dia in alertas:
    print([bloco, dia])