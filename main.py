import cfg, pygame, player, parts.base

clock = pygame.time.Clock()

p = player.player(parts.base.rocket)

while True:
    cfg.events.update()    
    cfg.win.fill((0,0,0))
    p.update()
    pygame.display.flip()
    clock.tick(60)
