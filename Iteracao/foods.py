my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_foods)
my_foods.append('cannoli')
friends_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_foods)

teste = friends_foods.copy()
print(teste)