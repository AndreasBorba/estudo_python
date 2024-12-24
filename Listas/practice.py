list_name = ['Manoel', 'Sinesio', 'Antonio', 'Fulano']

print(f"Senhor {list_name[0]}, você tem um convite para jantar. Você aceita?")
print(f"Senhor {list_name[1]}, você tem um convite para jantar. Você aceita?")
print(f"Senhor {list_name[2]}, você tem um convite para jantar. Você aceita?")
print(f"Senhor {list_name[3]}, você tem um convite para jantar. Você aceita?")

print(f"O senhor {list_name[3]} não poderá participar do evento.")

list_name[3] = 'Ito'
print(f"Senhor {list_name[3]}, você tem um convite para jantar. Você aceita?")

print(list_name)

list_name.insert(0, 'Fulano')
print(list_name)

list_name.insert(2, 'Ciclano')
print(list_name)

list_name.append('Shazam')
print(list_name)
print(len(list_name)-1)

print(f'O senhor {list_name.pop(0).title()} não poderá participar do evento')
print(list_name)
del list_name[-1] # Remove o último valor da lista devido ao -1
print(f"O senhor Shazam não poderá participar do evento.")
print(list_name)
nao_participante = 'ciclano'
list_name.remove(nao_participante.title())
print(f"O senhor {nao_participante.title()} não poderá participar do evento.")
print(list_name)

