import time
import pygame as pg
from settings import *
from Target import *
from Menu import *
from User import *


class Game:
    count = 0

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("comicsansms", 20)
        self.start_timestamp = 0
        self.end_timestmap = 0
        self.user = User(self)
        self.current_user = self.user.get_current_user()

    def new_game(self):
        self.target = Target(self)

    def update(self):
        pg.display.flip()

    def draw(self):
        self.target.draw()

    def display_user_menu(self):
        while True:
            user_menu = Menu(self, "User Menu")
            items_menu = ["Create User", "Change user", "Delete User"]
            user_menu.init_items(items_menu)
            user_menu.draw_menu()

            for event in pg.event.get():
                Helper.check_quit_game(event)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        self.current_user = self.user.create_user()
                    elif event.key == pg.K_2:
                        self.current_user = self.user.change_current_user()
                    elif event.key == pg.K_3:
                        self.user.delete_user()
                    elif event.key == pg.K_RETURN:
                        self.main_menu()
                        return

                # pg.display.flip()
                self.update()

    def display_level_menu(self):
        while True:
            self.menu = Menu(self, "Click Me ! -- Level Menu")
            items_menu = ["Level 1", "Level 2"]
            self.menu.init_items(items_menu)
            self.menu.draw_menu()

            for event in pg.event.get():
                Helper.check_quit_game(event)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        self.start_level_one()
                    if event.key == pg.K_RETURN:
                        self.main_menu()
                        return
            # pg.display.flip()
            self.update()

    def main_menu(self):
        main_menu = Menu(self, "Click Me - Main Menu")

        if self.current_user:
            menu_items = [
                f"Current user : {self.current_user}", "Choose game level"]

        else:
            menu_items = ["Create user"]
        main_menu.init_items(menu_items)
        main_menu.draw_menu()
        for event in pg.event.get():
            Helper.check_quit_game(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1 and not self.current_user:
                    self.user.create_user()
                if event.key == pg.K_1 and self.current_user:
                    self.display_user_menu()
                if event.key == pg.K_2 and self.current_user:
                    self.display_level_menu()

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

            Helper.check_quit_game(event)
            

    def start_level_one(self):
        self.start_timestamp = time.time()
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
        while True:
            self.new_game()
            while True:
                self.screen.fill((0, 0, 0))
                self.draw()
                self.update()
                self.check_events()

    def display_results_menu(self, time_score):
        while True:
            self.menu = Menu(self, "Click Me ! -- Results Menu")
            items_menu = [
                f"Your score: {time_score}- See all scores", "Go back to main menu"]
            self.menu.init_items(items_menu)
            self.menu.draw_menu()

            for event in pg.event.get():
                Helper.check_quit_game(event)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        self.display_10th_last_scores()
                    if event.key == pg.K_2:
                        self.start_game() 

            # pg.display.flip()
            self.update()

    def display_10th_last_scores(self):
        scores = self.user.get_10th_last_scores(self.current_user)
        while True:
            title = "Your 10th last scores"
            self.screen.fill((0, 0, 0))

            first_coor_menu = 100
            Helper.display_text(self, title, WIDTH/2, 80 - 50)
            for score in scores:
                Helper.display_text(
                    self, score["score"], WIDTH/2, first_coor_menu)
                first_coor_menu += 50
            for event in pg.event.get():
                Helper.check_quit_game(event)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.start_game()

            # pg.display.flip()
            self.update()

    def display_result(self):
        self.end_timestmap = time.time()
        time_score = round(self.end_timestmap - self.start_timestamp, 2)
        self.screen.fill((0, 0, 0))
        self.user.write_score(self.current_user, time_score)
        text_score = f"Your score is {time_score} seconds !"
        Helper.display_text(game, text_score, WIDTH/2, HEIGHT/2)
        Game.count = 0
        self.display_results_menu(time_score)


if __name__ == "__main__":
    game = Game()
    game.start_game()
