# Importando a biblioteca:

import random

# Interação com o usuário para recolher dados:

alunos = input ("Insira o nome de seus alunos para o sorteio: ")

# Transformando em lista:

lista_alunos = [nome.strip() for nome in alunos.split(",")]

# Sorteando o aluno:

sorteio = random.choice(lista_alunos)

# Informando o aluno sorteado:

print (f"O aluno sorteado é: {sorteio}! ")


