cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Organizando para ordem reversa

cars.sort(reverse=True)
print(cars)

car = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(car)
print("\nHere is the sorted list:")
print(sorted(car)) #Pode ser usado o parâmetro reverse=True
print("\nHere is the original list again:")
print(car)

car.reverse() #Tem o proposito de inverter a lista
print(f"{car}")

#Obtendo o tamanho de uma lista
print(f"\n{len(car)}")