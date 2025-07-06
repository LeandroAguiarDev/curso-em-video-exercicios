# Importar a bíblioteca necessária:

import math

# Interação com usuário para recolher dados:

an = float (input ("Digite o valor do ângulo (em graus) para calcular seno, cosseno e tangente: "))

# Convertendo graus para radianos:

ra = math.radians(an)

# Cálculando: 

se = math.sin(ra)
co = math.cos(ra)
ta = math.tan(ra)

# Informando o resultado ao usuário:

print (f"\nO Ângulo de {an}º, tem o seno {se:.4f}, cosseno {co:.4f} e tangente {ta:.4f}!" )

# Legendas
# an = ângulo
# ra = Radianos
# se = Seno
# co = Cosseno
# ta = Tangente
