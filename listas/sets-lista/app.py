list1 = [10,20,30,60]
list2 = [10,20,55,13]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # mostra todos os numeros sem repetições
print(num1 - num2) # mostra os numeros diferentes
print(num1 ^ num2) # mostra os numeros que nao sao repetidos
print(num1 & num2) # mostra os repetidos