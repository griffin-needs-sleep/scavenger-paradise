import cfg, pygame, vectors


class obj:
    def __init__(self, collision:bool, surf:pygame.surface.Surface, pos:vectors.vec) -> None:
        self.collision = collision
        self.surf = surf
        self.hb = surf.get_rect()
        self.pos = pos
        cfg.obs.append(self)
    
    def update(self) -> None:
        cfg.win.blit(self.surf, tuple(self.pos))


class box(obj):
    def __init__(self, pos:vectors.vec) -> None:
        surf = pygame.surface.Surface((200,200))
        surf.fill((200,200,200))
        super().__init__(True, surf, pos)
    