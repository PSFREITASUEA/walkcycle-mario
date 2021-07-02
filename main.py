import pygame
from pygame import KEYDOWN, K_LEFT, K_RIGHT, KEYUP, K_a, K_d, K_SPACE

from Player import Player
from utils import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(30, WINDOW_HEIGHT - 250)

    isRunning = True

    while isRunning:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.is_going_left = True
                elif event.key == K_RIGHT:
                    player.is_going_right = True
                elif event.key == K_a:
                    player.is_running_left = True
                elif event.key == K_d:
                    player.is_running_right = True
                elif event.key == K_SPACE:
                    player.is_jump = True

            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    player.is_going_left = False
                    player.is_idle_to_left = True
                    player.is_idle_to_right = False
                elif event.key == K_RIGHT:
                    player.is_going_right = False
                    player.is_idle_to_left = False
                    player.is_idle_to_right = True
                elif event.key == K_a:
                    player.is_idle_to_left = True
                    player.is_idle_to_right = False
                    player.is_running_left = False
                elif event.key == K_d:
                    player.is_idle_to_left = False
                    player.is_idle_to_right = True
                    player.is_running_right = False

        player.update()
        player.render(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))

