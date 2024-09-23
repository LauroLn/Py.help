valor = int(input("Digite o valor do produto: "))
valor2 = 25

while valor > 20:
    valor = (valor *0.10) + valor
    print(f"o valor final do produto é de R${valor}")
    break

#vi que dava pra fazer com o if 
if valor2 > 20:
    valor2 = (valor2 *0.10) + valor2
    print(f"VALOR é DE {valor2}")