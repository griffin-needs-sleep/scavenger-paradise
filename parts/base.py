from vectors import vec
import pygame, cfg, pixel_art
import parts.part as part

"handles movment"



class base(part.part):
    pass

class rocket(base):
    image = pixel_art.rocket
    def update(player):
        for key in cfg.events.keys:
            match key:
                case pygame.K_w:
                    player.vel.y-=player.speed
                case pygame.K_s:
                    player.vel.y+=player.speed
                case pygame.K_a:
                    player.vel.x-=player.speed
                case pygame.K_d:
                    player.vel.x+=player.speed
        player.vel *= 0.970

        #n_hb = pygame.rect.Rect(player.pos.x, player.pos.y, )
        #u_hb

        #for ob in cfg.obj:

        player.pos += player.vel
        player.rot = -player.vel.x*1.5

