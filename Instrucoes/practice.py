car = 'subaru'
print("Is car == 'subaru'? I predict True.")

print('Is car == "audi" ? I predict False.')
print(car == 'audi')

if car.lower() == 'subaru':
    print('Voce acertou')
else:
    print('Voce errou')

idade = input('Digite sua idade: ')
if idade >= '18':
    print('Voce é maior de idade. Pode entrar.')
elif idade >= '16' and idade <= '17':
    print('Voce é menor de idade')
    print('Mas pode entrar acompanhado de um responsavel')
else:
    print('Voce é menor de idade e não pode entrar acompanhado de um responsavel')

arvores = ['pau-brasil', 'ipê', 'jacarandá', 'cerejeira', 'cerejeira']
if 'cerejeira' in arvores or 'jacarandá' in arvores:
    print('Cerejeira ou jacarandá estão na lista')
