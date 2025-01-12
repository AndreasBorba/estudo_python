players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f'Os três primeiros elementos da lista são: {players[0:3]}')
print(f'Os três elementos do meio da lista são: {players[1:4]}')
print(f'Os três últimos elementos da lista são: {players[-3:]}')

friend_pizza = ['pepperoni', 'marguerita', 'calabresa', 'portuguesa']
my_pizza = friend_pizza.copy()
friend_pizza.append('4 queijos')
my_pizza.append('baiana')
print('My favorite pizzas are:')
for pizza in my_pizza:
    print(f'- {pizza.title()}')
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(f'- {pizza.title()}')

