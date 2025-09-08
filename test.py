import cfg, pygame, player, parts.base, parts.weapon, parts.body

clock = pygame.time.Clock()





p = player.player(parts.base.rocket, parts.body.basic, parts.weapon.fist)



while True:
    cfg.events.update()    
    cfg.win.fill((0,0,0))
    p.update()
    pygame.display.flip()
    clock.tick(60)
