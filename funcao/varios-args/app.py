def soma(*numeros): #* define que podem ser varios numeros
    total = 0
    for num in numeros:
  
        total += num
    return total

x = soma(2,5,8,13,2)

print(x)