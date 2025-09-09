from vectors import *
import cfg, pygame
from parts import base, body, weapon, head




class player:
    def __init__(self, base:base.base, body:body.body, weapon:weapon.weapon, head:head.head):
        self.head = head
        self.base = base
        self.body = body
        self.weapon = weapon
        self.pos = vec(0,0)
        self.vel = vec(0,0)
        self.speed = 0.5
        self.rot = 0
        self.hb = pygame.rect.Rect(0,0,8*cfg.img_scaling, 20*cfg.img_scaling)
        self.surf = pygame.surface.Surface((8*cfg.img_scaling, 20*cfg.img_scaling), pygame.SRCALPHA).convert_alpha()

    def update(self):
        self.base.update(self)
        self.hb.center = tuple(self.pos)
        self.draw()        
        pygame.draw.rect(cfg.win, (255,0,0), self.hb, 1)


    def draw(self):
        self.surf.fill((0,0,0))
        self.surf.blit(self.body.image, (0,0))
        self.surf.blit(self.base.image, (0, 10*cfg.img_scaling))

        surf = pygame.transform.rotate(self.surf, self.rot)
        rect = surf.get_rect()

        rect.center = self.hb.center
        cfg.win.blit(surf,  rect.topleft)




    



        