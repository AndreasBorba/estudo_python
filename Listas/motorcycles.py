motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('kawasaki')
print(motorcycles)

motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')
print(motorcycle)
motorcycle.insert(0, 'ducati') #Insiro o valor de acordo com a posição desejada
motorcycle.insert(7, 'kawasaki') # Ocorre uma ordenação automática, não inserindo necessariamente na posição em que foi informado
motorcycle.insert(6, 'shineray')
print(motorcycle)
del motorcycle[0]
print(motorcycle)
#POP
popped_motorcycle = motorcycle.pop();
print(motorcycle)
print(popped_motorcycle)
print(motorcycle)

#É possível remover qualquer elemento da lista informando qual sua posição
print(motorcycles)
print(f'The first motorcycle I owned was a {motorcycles.pop(0).title()}.')

#Removendo um elemento por valor
print(motorcycle)
motorcycle.remove('honda')
print(motorcycle)
