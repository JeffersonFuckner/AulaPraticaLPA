import random

import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name] + random.randint(0,100)
            return EnemyShot(f'{self.name}Shoot', position=(self.rect.centerx, self.rect.centery))
