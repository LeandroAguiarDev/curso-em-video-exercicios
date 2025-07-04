#boas-vindas e pedido para inserir o valor em metros

print ("Olá, bem-vindo(a)! Sou um conversor de Metros para centímetros e milímetros! ")
m = float (input ("Insira um valor em metros para a conversão: "))

#resolução para aprensentar na tela

print ("O seu valor é {} metros, em centímetros é: {:.2f} CM, em milímetros é: {:.2f} MM! ".format(m, (m * 100), (m * 1000)))
