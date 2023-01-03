import pygame as pg


class Helper:

    @staticmethod
    def display_text(game, text, coor_x, coor_y):
        font = game.font.render(text, True, (255, 0, 0))
        font_rect = font.get_rect()
        font_rect.center = (coor_x, coor_y)
        game.screen.blit(font, font_rect)
