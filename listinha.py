import random

lista_nome = []
quantidade = int(input("Quantas pessoas estão na equipe: "))

for i in range(quantidade):
	nome = input(f"digite o nome da pessoa {i+1}:")
	lista_nome.append(nome)

print(lista_nome)

print("-"*30)
print("A equipe (em ordem) será de:")
random.shuffle(lista_nome)
for nomes in lista_nome:
	print(nomes)
print("-"*30)
