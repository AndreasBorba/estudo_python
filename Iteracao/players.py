players = ['ronaldo', 'messi', 'neymar', 'mbappe', 'hazard']
print(players[1:3])

#Caso omita o primeiro índice, o Python automaticamente 
#começa no início da lista
print(players[:3])
#Isso serve para o mesmo caso do último índice
print(players[2:])
#Exibindo os 3 últimos jogadores
print(players[-3:])
print(players[:-3])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
