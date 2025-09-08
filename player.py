from vectors import *
import cfg, pygame




class player:
    def __init__(self, base):
        self.base = base


    def update(self):
        self.base.update()
        pygame.draw.rect(cfg.win, (255,255,255), (*self.base.pos, 100,100))



        