import pygame.image

from SpriteLoader import *
from utils import *


class Player:
    def __init__(self, pos_x, pos_y):
        self.sprites_walk_right = load_sprites_walk_right()
        self.sprites_run_right = load_sprites_run_right()
        self.sprites_walk_left = load_sprites_walk_left()
        self.sprites_run_left = load_sprites_run_left()
        self.sprites_jump_left = load_sprites_jump_left()
        self.sprites_jump_right = load_sprites_jump_right()
        self.current_left = 0
        self.current_run_left = 0
        self.current_right = 0
        self.current_run_right = 0
        self.current_jump_left = 0
        self.current_jump_right = 0
        self.image = self.sprites_walk_right[self.current_right]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos_x, pos_y)
        self.is_idle_to_left = False
        self.is_idle_to_right = True
        self.is_going_up = False
        self.is_going_left = False
        self.is_going_right = False
        self.is_running_left = False
        self.is_running_right = False
        self.is_jump = False
        self.jump_count = 10

    def movement(self):
        if not self.is_jump:
            if self.is_going_right:
                self.rect.x += 5
            elif self.is_going_left:
                self.rect.x -= 5
            elif self.is_running_left:
                self.rect.x -= 12
            elif self.is_running_right:
                self.rect.x += 12
        else:
            if self.jump_count >= -10:
                self.rect.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                if self.is_going_left:
                    self.rect.x -= 5
                elif self.is_going_right:
                    self.rect.x += 5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jump = False

    def update(self):
        self.movement()
        self.animate()
        self.is_colliding_with_limits()

    def render(self, screen: pygame.surface):
        if self.is_going_right:
            screen.blit(self.sprites_walk_right[int(self.current_right)], (self.rect.x, self.rect.y))
        elif self.is_going_left:
            screen.blit(self.sprites_walk_left[int(self.current_left)], (self.rect.x, self.rect.y))
        elif self.is_running_right:
            screen.blit(self.sprites_run_right[int(self.current_run_right)], (self.rect.x, self.rect.y))
        elif self.is_running_left:
            screen.blit(self.sprites_run_left[int(self.current_run_left)], (self.rect.x, self.rect.y))
        elif self.is_idle_to_left:
            if self.is_jump:
                screen.blit(self.sprites_jump_left[int(self.current_jump_left)], (self.rect.x, self.rect.y))
            else:
                screen.blit(self.sprites_walk_left[2], (self.rect.x, self.rect.y))
        elif self.is_idle_to_right:
            if self.is_jump:
                screen.blit(self.sprites_jump_right[int(self.current_jump_right)], (self.rect.x, self.rect.y))
            else:
                screen.blit(self.sprites_walk_right[2], (self.rect.x, self.rect.y))

    def is_colliding_with_limits(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def animate(self):
        if self.is_going_right:
            self.current_right += 0.25
            if self.current_right >= len(self.sprites_walk_right):
                self.current_right = 1
        elif self.is_going_left:
            self.current_left += 0.25
            if self.current_left >= len(self.sprites_walk_left):
                self.current_left = 1
        elif self.is_running_left:
            self.current_run_left += 0.5
            if self.current_run_left >= len(self.sprites_run_left):
                self.current_run_left = len(self.sprites_run_left) - 5
        elif self.is_running_right:
            self.current_run_right += 0.5
            if self.current_run_right >= len(self.sprites_run_right):
                self.current_run_right = len(self.sprites_run_right) - 5
        elif self.is_jump:
            if self.is_idle_to_right:
                self.current_jump_right += 0.25
                if self.current_jump_right >= len(self.sprites_jump_right):
                    self.current_jump_right = len(self.sprites_jump_right) - 1
            elif self.is_idle_to_left:
                self.current_jump_left += 0.25
                if self.current_jump_left >= len(self.sprites_jump_left):
                    self.current_jump_left = len(self.sprites_jump_left) - 1
        else:
            self.current_left = 0
            self.current_right = 0
            self.current_run_left = 0
            self.current_run_right = 0
            self.current_jump_left = 0
            self.current_jump_right = 0
