#boas-vindas e pedido para inserir o valor em metros

print ("Olá, bem-vindo(a)! Sou um conversor de Metros para centímetros e milímetros! ")
m = float (input ("Insira um valor em metros para a conversão: "))

#realizar a conversão

cm = m * 100
mm = m * 1000

#resolução para aprensentar na tela

print ("O seu valor é {} metros, em centímetros é: {} CM, em milímetros é: {} MM! ".format(m, cm, mm))


