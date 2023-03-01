conjunto1 = set(range(1, 15))
conjunto2 = set(range(10, 20))
conjunto3 = set(range(14, 25))

print(conjunto1.difference(conjunto2))
print(conjunto1.intersection(conjunto2))


# dicionários
agenda = {}
agenda['orlando'] = ['Eng. Sof1', 'Des. Web 2', 'Des. Web 3']
agenda['nilton'] = ['Algoritmos', 'Banco de Dados Relacional']
agenda['jose'] = '(19) 99999-9999'
# try:
#     print(agenda['Orlando'])
# except KeyError:
#     print('Não encontrado')
# ou...
print(agenda.get('orlando', 'Não encontrado'))
print(agenda.get('Orlando', 'Não encontrado'))

print(agenda.keys())
print(list(agenda.keys()))
for chave in agenda:
    print('Chave => ' + chave)
    print(agenda[chave])
    print('')