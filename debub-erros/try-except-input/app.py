
#try:
 #   valor = int(input("digite o valor do seu produto: "))
 #   print(valor)
#except ValueError:
#    print('Aconteceu uma falha...')
#    print('Digite em numeros')
#    print(f'Erro: {ValueError}')
#print('codigo continua...')


#try:
 #   idade = int(input("Digite a sua idade: "))
  #  print(idade)
#except ValueError:
    #while ValueError:
        #idade = int(input("Digite a sua idade em numero: "))
        #print(idade)


while True: # quebrei um pouco a cabeça para entender, mas utilizamos um estrutura de repetição para que verifique com o try a condição e persista 
    #ate que o codigo funcione
    try:
        idade = int(input("Digite a sua idade: "))
        print(idade)
        break
    except ValueError:
        print('Digite um numero valido')

for tentativa in range(3):# mesma coisa porem com o for e limitando o numero de tentativas
    try:
        idade = int(input("Digite a sua idade: "))
        print(idade)
    except ValueError:
        print("Digite um numero: ")
else: 
    print("Numero maximo de tentativas")