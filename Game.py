import pygame as pg
import sys
from settings import *
from Target import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("forte", 20)

    def new_game(self):
        self.target = Target(self)

    def update(self):
        pg.display.flip()

    def draw(self):
        self.target.draw()

    def display_text(self, text, coor_x, coor_y):
        font = self.font.render(text, True, (255, 0, 0))
        font_rect = font.get_rect()
        font_rect.center = (coor_x, coor_y)
        self.screen.blit(font, font_rect)

    def main_menu(self):
        self.display_text("Click Me !", 500, HEIGHT/2 - 50)
        self.display_text("Level 1", 500, HEIGHT/2)
        self.display_text("Level 2", 500, HEIGHT/2 + 50)
        self.display_text("Level 3", 500, HEIGHT/2 + 100)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                self.game_loop()
        pg.display.flip()

    def quit_game(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                self.game_loop()

    def start_game(self):
        self.screen.fill((0, 0, 0))
        while True:
            self.main_menu()
            self.update()
            self.clock.tick(FPS)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if self.target.target_img_rect.collidepoint(pos):
                    self.target.update()
                print(pos)

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def game_loop(self):
        print("ok")
        while True:
            self.new_game()
            while True:
                self.screen.fill((0, 0, 0))

                self.draw()
                self.update()
                self.check_events()


if __name__ == "__main__":
    game = Game()
    game.start_game()
