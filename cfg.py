import pygame


win_size = (500,500)
win = pygame.display.set_mode(win_size)

class events_(type):    
    def __iter__(cls):
        return cls.events.__iter__()
    
class events(metaclass=events_):
    events = []
    keys = set()

    @classmethod
    def update(cls):
        cls.events = pygame.event.get()
        for event in cls.events:

            if event.type == pygame.KEYDOWN:
                cls.keys.add(event.key)

            if event.type == pygame.KEYUP:
                cls.keys.remove(event.key)

            if event.type == pygame.QUIT:
                pygame.quit()
