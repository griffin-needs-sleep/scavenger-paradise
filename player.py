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

    def update(self):
        self.base.update(self)
        pygame.draw.rect(cfg.win, (255,255,255), (*self.pos, 100,100))



        