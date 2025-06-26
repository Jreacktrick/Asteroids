#this allows us to use code from the open-source pygame library
import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return
        updatable.update(dt)
        for object in asteroids:
            if object.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if object.collision(shot):
                    shot.kill()
                    object.split()

        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        dt += clock.tick(60) / 1000
            

if __name__ == "__main__":
    main()
