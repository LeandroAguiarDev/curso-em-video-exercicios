print ("Olá, eu sou um programa que lê um número e mostra o seu Dobro, Triplo e a sua Raiz Quadrada. ")

n = float (input ("Por favor, insira um número: "))

d = n * 2 
t = n * 3
rq = n ** 2

print ("Seu número escolhido é o {}, seu dobro é: {}, seu triplo é: {},".format(n, d, t), end=" ")
print ("e sua raiz quadrada é: {}".format(rq))

