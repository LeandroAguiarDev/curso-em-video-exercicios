# Importando a biblioteca para o programa:

import math

# Pedido as informações ao usuário:

print ("Olá, sou uma calculadora de hipotenusa ")

co = float (input ("Por favor, insira o cateto oposto: "))
ca = float (input ("Agora, o cateto adjacente: "))

# Informando na tela do usuário

print (f"\nA hipotenusa é: {math.hypot(co, ca):.2f} ")

# Legendas:
# co = Cateto oposto
# ca = Cateto adjacente
