aluno = {'nome':'Lauro', 'nota':10, 'idade': 19, 'aprovacao': True}

aluno.update({'nome':'José', 'nota':9})# update podemos alterar mais de uma coisa de uma vez
#aluno['nome'] = 'Livia'
#aluno.update({'endereco': 'Rua sao mateus'})

#print(aluno.get('endereco', "Nao existe"))

del aluno['idade']

print(aluno)
