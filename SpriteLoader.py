import pygame

from utils import DEFAULT_IMAGE_SIZE


def load_sprites_walk_right():
    sprites_walk_right = []
    for number_sprite in range(1, 13):
        sprites_walk_right.append(
            pygame.transform.scale(
                pygame.image.load(f'assets/walk_right_{number_sprite}.png'),
                DEFAULT_IMAGE_SIZE
            )
        )
    return sprites_walk_right


def load_sprites_run_left():
    sprites_run_left = []
    for number_sprite in range(1, 18):
        sprites_run_left.append(
            pygame.transform.scale(
                pygame.image.load(f'assets/run_left_{number_sprite}.png'),
                DEFAULT_IMAGE_SIZE
            )
        )
    return sprites_run_left


def load_sprites_run_right():
    sprites_run_right = []
    for number_sprite in range(1, 18):
        sprites_run_right.append(
            pygame.transform.scale(
                pygame.image.load(f'assets/run_right_{number_sprite}.png'),
                DEFAULT_IMAGE_SIZE
            )
        )
    return sprites_run_right


def load_sprites_walk_left():
    sprites_walk_left = []
    for number_sprite in range(1, 13):
        sprites_walk_left.append(
            pygame.transform.scale(
                pygame.image.load(f'assets/walk_left_{number_sprite}.png'),
                DEFAULT_IMAGE_SIZE
            )
        )
    return sprites_walk_left


def load_sprites_jump_left():
    sprites_jump_left = []
    for number_sprite in range(1, 11):
        sprites_jump_left.append(
            pygame.transform.scale(
                pygame.image.load(f'assets/jump_left_{number_sprite}.png'),
                DEFAULT_IMAGE_SIZE
            )
        )
    return sprites_jump_left


def load_sprites_jump_right():
    sprites_jump_right = []
    for number_sprite in range(1, 11):
        sprites_jump_right.append(
            pygame.transform.scale(
                pygame.image.load(f'assets/jump_right_{number_sprite}.png'),
                DEFAULT_IMAGE_SIZE
            )
        )
    return sprites_jump_right
