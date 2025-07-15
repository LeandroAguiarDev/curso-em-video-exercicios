# Interação para receber dados: 

dados = input ("Qual é o seu nome completo? ")

# Usando as operações:

print (f"\nSeu nome com tudo em maiúsculo: {dados.upper()}")
print (f"Seu nome com tudo em minúsculo: {dados.lower()}")
print (f"Seu nome tem um total de {len(dados)} letras com espaços.")
print (f"Seu nome completo tem um total de {len(dados.replace(' ',''))} letras sem espaçoes.")

# Calculando o primeiro nome:

primeiro_nome = dados.split()[0]
print (f"Seu primeiro nome tem um total de {len(primeiro_nome)} letras.")

