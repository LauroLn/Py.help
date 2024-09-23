aluno = {
    'nome':'Lauro', 
    'nota':10, 'idade': 19, 
    'aprovacao': True, 
    'materias': ['Fisica','Matematica','Portugues']
         }

print(aluno)


print('-------------')


#print(aluno['materias'])
print(aluno.get('materias'))
print(len(aluno['materias']))
print(len(aluno))

print('-------------')

print(aluno.items())
print(aluno.keys())
print(aluno.values())