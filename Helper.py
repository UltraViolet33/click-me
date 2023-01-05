import pygame as pg
import sys


class Helper:

    @staticmethod
    def display_text(game, text, coor_x, coor_y):
        font = game.font.render(text, True, (255, 0, 0))
        font_rect = font.get_rect()
        font_rect.center = (coor_x, coor_y)
        game.screen.blit(font, font_rect)

    @staticmethod
    def display_input(game):
        font = pg.font.Font(None, 32)
        input_rect = pg.Rect(200, 200, 140, 32)
        color = pg.Color('lightskyblue3')
        user_text = ""
        while True:
            game.screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pg.K_RETURN:
                        print(user_text)
                        return user_text
                    else:
                        user_text += event.unicode

            pg.draw.rect(game.screen, color, input_rect)
            text_surface = font.render(user_text, True, (255, 255, 255))
            game.screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+10)
            pg.display.flip()
