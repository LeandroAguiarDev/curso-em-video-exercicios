# Interação com o usuário para receber as informações

da = int (input ("Quantos dias o cliente ficou com o carro? "))
km = float (input ("Quantos KMs foram rodados? "))

# Cálculando o valor:

# da * 60
# km * 0.15
# t = da + dr

# Informar o resultado para o usuário

print ("O valor a ser pago é de R${:.2f}, por {} dias alugados com {}kms rodados! ".format((da * 60)+(km * 0.15), da, km))

# Legendas
# da = Dias alugados
# km = KMs rodados
