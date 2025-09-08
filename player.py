from vectors import *
import cfg, pygame
from parts import base, body, weapon




class player:
    def __init__(self, base:base.base, body:body.body, weapon:weapon.weapon):
        self.base = base
        self.body = body
        self.weapon = weapon
        self.pos = vec(0,0)
        self.vel = vec(0,0)
        self.speed = 0.5
        self.surf = pygame.surface.Surface((8*cfg.img_scaling, 20*cfg.img_scaling))
        self.update_surf()

    def update(self):
        self.base.update(self)
        cfg.win.blit(self.surf,  tuple(self.pos))
        pygame.draw.rect(cfg.win, (255,0,0), (*self.pos, 8*cfg.img_scaling, 20*cfg.img_scaling), 1)


    def update_surf(self):
        self.surf.fill((0,0,0))
        self.surf.blit(self.body.image, (0,0))
        self.surf.blit(self.base.image, (0, 10*cfg.img_scaling))



    



        