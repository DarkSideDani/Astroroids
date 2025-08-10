import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip() # display update
        dt = clock.tick(60) / 1000 # limit the FPS to 60
        



if __name__ == "__main__":
    main()
