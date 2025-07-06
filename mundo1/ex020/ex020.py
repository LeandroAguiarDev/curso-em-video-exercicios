# Importando a biblioteca:

import random 

# Recebendo dados do usuário:

alunos = input ("Insira o nome dos alunos: ")

# Criando a lista:

lista_alunos = [name.strip() for name in alunos.split (",")]

# Realizando o sorteio:

random.shuffle(lista_alunos)

# Informando ao usuário:

print (f"A sequência dos alunos sorteados é: " )
for i, alunos in enumerate(lista_alunos, start=1):
    print (f"{i}º: {alunos}")



