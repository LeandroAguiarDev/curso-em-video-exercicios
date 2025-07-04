#aprentação do programa

print ("Bem-vindo(a)! Sou uma calculadora de tinta para parede. ")
print ("Com 1L de tinta, você consegue pintar 2m²")

#Interação para receber os dados

p1 = float (input ("Qual a largura da parede? "))
p2 = float (input ("Qual a altura da parede? "))

#calculando os metros

m = p1 * p2 

#calculando a quantidade de tinta necessária

t = m / 2

#resultado na tela do usuário

print ("A sua parede precisa de {:.2f}L de tinta, com um total de {:.2f}m²".format(t, m))

