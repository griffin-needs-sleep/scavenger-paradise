from vectors import vec
import pygame, cfg

class base:
    pos = vec(0,0)
    vel = vec(0,0)

class rocket(base):
    speed=0.005
    
    @classmethod
    def update(cls):
        for key in cfg.events.keys:
            match key:
                case pygame.K_w:
                    cls.vel.y-=cls.speed
                case pygame.K_s:
                    cls.vel.y+=cls.speed
                case pygame.K_a:
                    cls.vel.x-=cls.speed
                case pygame.K_d:
                    cls.vel.x+=cls.speed
        cls.vel *= 0.995
        cls.pos += cls.vel
        

                


