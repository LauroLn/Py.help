compra_confirmada = True
dados_compra = "Compra no valor de 12,59"


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviados para o seu e-mail")
        break
    else:
        print('Falha na compra')
        break
