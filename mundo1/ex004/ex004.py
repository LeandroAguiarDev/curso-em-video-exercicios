print ("Insira uma palavra ou um número para que eu tente indentificar as suas caracteristicas. ")

in1 = input ("Insira uma palavra ou um número: ")

print ("O que você inseriu é: {}".format(in1))
print ("Tipo primitivo: {}".format(type(in1)))
print ("É alfanumérico? {}".format(in1.isalnum()))
print ("É alfabético? {}".format(in1.isalpha()))
print ("É decimal? {}".format(in1.isdecimal()))
print ("É numérico? {}".format(in1.isnumeric()))
print ("É imprimível? {}".format(in1.isprintable()))
print ("Está em maiúsculas? {}".format(in1.isupper()))
print ("Está em minúsculas? {}".format(in1.islower()))