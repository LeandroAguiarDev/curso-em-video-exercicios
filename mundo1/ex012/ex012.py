#Interação com o usuario para receber o valor

print ("Olá, vamos calcular seu desconto de 5% ")
pp = float (input ("Insira o valor do produto sem o desconto: "))

#informando ao usuario o resultado final.

#ds = pp * 0.05
#vf = pp - ds

print ("Seu produto com desconto de 5% irá ficar o total de R${:.2f} ".format(pp - (pp * 0.05)))

#legendas:
# pp = preço do produto
# ds = desconto do produto
# vf = valor final do produto. 
