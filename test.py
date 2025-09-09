import cfg, pygame, player, objects
from parts import base, body, weapon, head
from vectors import *
clock = pygame.time.Clock()



objects.box(vec(400,300))

p = player.player(base.rocket, body.basic, weapon.fist, head.head)



while True:
    cfg.events.update()    
    cfg.win.fill((0,0,0))
    p.update()
    [ob.update() for ob in cfg.obs]
        
    pygame.display.flip()
    clock.tick(60)
