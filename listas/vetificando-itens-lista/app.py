cor = input("Digite a cor desejada: ")


cores= ["vermelho", "azul","preto", "roxo"]

if cor.lower() in cores:
    print("Em estoque")
else:
    print("Fora do estoque")