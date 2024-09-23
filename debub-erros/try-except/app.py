try:
    letras = ['a', 'b', 'c'] 
    print(letras[3])#trabalhamos o erro, separando ele para modermos mexer,
except IndexError:#apos testar o index[3](nao existe) eu pego o nome do erro e coloco no except
    print("O Index nao existe")
  
