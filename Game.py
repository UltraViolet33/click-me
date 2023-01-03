import pygame as pg
import sys
from settings import *
from Target import *
import time
from Menu import *


class Game:
    count = 0

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("forte", 20)
        self.start_timestamp = 0
        self.end_timestmap = 0

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
        self.menu = Menu(self, "Click Me ! -- Main Menu")
        items_menu = ["Level 1", "Level 2"]
        self.menu.init_items(items_menu)
        self.menu.draw_menu()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_1:
                    self.start_level_one()
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
            if event.type == pg.MOUSEBUTTONUP and Game.count < 20:
                pos = pg.mouse.get_pos()
                if self.target.target_img_rect.collidepoint(pos):
                    self.target.update()
                    Game.count += 1
                    print(Game.count)
                print(pos)

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def start_level_one(self):
        self.start_timestamp = time.time()
        print(self.start_timestamp)
        print("lelvel 1")
        while True:
            self.new_game()
            while True:
                self.screen.fill((0, 0, 0))
                self.draw()
                self.update()
                if Game.count < 3:
                    self.check_events()
                else:
                    self.display_result()

    def game_loop(self):
        print("ok")
        while True:
            self.new_game()
            while True:
                self.screen.fill((0, 0, 0))
                self.draw()
                self.update()
                self.check_events()

    def display_result(self):
        print("ok")
        self.end_timestmap = time.time()
        time_score = self.end_timestmap - self.start_timestamp
        print(time_score)
        self.screen.fill((0, 0, 0))
        text_score = f"Your score is {round(time_score, 2)} seconds !"
        self.display_text(text_score, WIDTH/2, HEIGHT/2)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    # game_loop()
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.start_game()
