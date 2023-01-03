import pygame as pg
from Helper import *
from settings import *


class Menu:
    def __init__(self, game, main_text):
        self.game = game
        self.main_text = main_text

    def init_items(self, items_menu):
        self.items_menu = items_menu

    def draw_menu(self):
        first_coor_menu = HEIGHT/2
        Helper.display_text(self.game, self.main_text, WIDTH/2, HEIGHT/2 - 50)
        for item in self.items_menu:

            Helper.display_text(
                self.game, item, WIDTH/2, first_coor_menu)
            first_coor_menu += 50

