import pygame as pg
import sys
from settings import *
from Target import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

    def new_game(self):
        self.target = Target(self)

    def update(self):
        pg.display.flip()

    def draw(self):
        self.target.draw()

    def main_menu(self):
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
