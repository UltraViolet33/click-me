import pygame as pg
from settings import *
import random


class Target:
    def __init__(self, game):
        self.game = game
        self.target_img = pg.image.load("./images/target.png")
        self.target_img_rect = self.target_img.get_rect()
        self.target_img_rect.left = WIDTH / 2
        self.target_img_rect.top = HEIGHT / 2

    def draw(self):
        self.game.screen.blit(self.target_img, self.target_img_rect)

    def update(self):
        width = self.target_img_rect.w
        height = self.target_img_rect.h
        self.target_img_rect.left = random.randint(width, WIDTH - width)
        self.target_img_rect.top = random.randint(height, HEIGHT - height)
