import pygame, cfg



bases = pygame.image.load("assets/bases.png").convert_alpha()
bodys = pygame.image.load("assets/bodys.png").convert_alpha()

basic  = pygame.transform.scale_by(bodys.subsurface(0,0,8,10), cfg.img_scaling)
rocket = pygame.transform.scale_by(bases.subsurface(0,0,8,10), cfg.img_scaling)