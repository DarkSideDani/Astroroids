import pygame
import time
from constants import *
from player import Player

def show_splash(screen):
    splash = pygame.image.load("Astroroids.png")
    splash = pygame.transform.scale(splash, (1280,720))
    screen.fill((0,0,0))
    screen.blit(splash, (0,0))
    pygame.display.flip()
    
    start_time = time.time()
    while time.time() - start_time < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    show_splash(screen)
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
