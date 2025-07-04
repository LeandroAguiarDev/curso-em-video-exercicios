#Interação com o usuário para receber o valor

print ("Olá, vamos calcular o novo salário com aumento de 15% ")
sl = float (input ("Insira o salário atual do funcionário "))

#Cálculo do novo salário

#au = sl * 0.15
#nl = sl + au

#Informando o novo salário

print ("Parabéns! o novo salário do seu funcionário é de R${:.2f}".format(sl + (sl * 0.15)))

#Legendas:
#sl = Salário
#au = Aumento do salário
#nl = Novo Salário.