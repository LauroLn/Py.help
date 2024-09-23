lista = [1,2,3,4]

def multi(x):
    return x * 2

lista2 = map(multi, lista)

print(list(lista2))