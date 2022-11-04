import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("LFE_Futebol_Pong")

loop = True

while loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False    
    
    pygame.display.update()