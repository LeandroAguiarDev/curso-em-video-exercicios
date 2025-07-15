# Importando arquivos necessários:

import pygame 

# Criando o player:

pygame.mixer.init()
pygame.mixer.music.load('AllMyProjects/aula_curso_em_video/mundo1/ex021/música/O Verão - Presto  ( As 4 Estações ) Antonio Vivaldi (1).mp3')
pygame.mixer.music.play()

# Evitar o fechamento imediatamente do programa:

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

