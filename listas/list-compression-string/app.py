frutas = ['banana', 'abacate', 'kiwi', 'morango']
#frutas2 = []

#for iten in frutas:
#    if 'n' in iten:
#        frutas2.append(iten)

frutas2 = [iten for iten in frutas if 'n' in iten]

print(frutas2)