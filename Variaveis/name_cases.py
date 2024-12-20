name = "eric";
message = f"Olá {name.title()}, gostaria de aprender um pouco de Python hoje?"
print(message)

message = f"Como gostaria de chamado? {name.upper()}, {name.lower()} ou {name.title()}?"
print(message)

message = "Albert Einstein disse uma vez: \"Uma pessoa que nunca cometeu um erro nunca tentou nada de novo\""
print(message)

full_name = "Albert Einstein"
message = f"{full_name} disse uma vez: \"Uma pessoa que nunca cometeu um erro nunca tentou nada de novo\""
print(message)

full_name = f"\t{full_name}\t"
print(full_name)
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())

#removeprefix() remove string no inicio da frase e removesuffix() no final da frase

name_file = "python_notes.txt"
print(name_file.removesuffix(".txt"))
print(name_file.removeprefix(".txt")) #Note que como não esta no inicio da frase, a ação é nula
