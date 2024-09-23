def cliente(n):
    print(f"olá {n}")
#so mostra o print, nao armazena o valor
#se apenas vai mostrar na tela algo use o print

def cliente2(n):
    return f"olá {n}"#com o return nos armazenamos o valor na função
# se vai utilizar o dado para outra coisa alem de mostrar na tela, use o return


cliente("Lauro")
print(cliente2("Pedro"))

#exemplo disso na pratica

x = cliente("Lauro")
y = cliente2("pedro")

print(x)
print(y)