for value in range(1, 21):
    print(value)

one_million = [value for value in range(1, 1000001)]
#for value in one_million:
#    print(value)

print(f'O menor número é: {min(one_million)}')
print(f'O maior número é: {max(one_million)}')
print(f'A soma de todos os números é: {sum(one_million)}')

numero_impar = [value for value in range(1, 21, 2)]
for value in numero_impar:
    print(f'O número {value} é impar.')

tres = [value for value in range(3, 31, 3)]
for value in tres:
    print(value)

cubos = [value ** 3 for value in range(1, 11)]
for value in cubos:
    print(value)

list_cubos = [value ** 3 for value in range(1, 11)]
print(list_cubos)