import pygame as pg
import sys
from settings import *
from Target import *
import time
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

    def new_game(self):
        self.target = Target(self)

    def update(self):
        pg.display.flip()

    def draw(self):
        self.target.draw()

    def display_user_menu(self):
        while True:
            user_menu = Menu(self, "User Menu")
            items_menu = ["Create User", "Delete User"]
            all_users = self.user.get_all_users()
            items_menu.extend(all_users)
            user_menu.init_items(items_menu)
            user_menu.draw_menu()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    if event.key == pg.K_1:
                        print("create user")
                        self.user.create_user()
                    elif event.key == pg.K_2:
                        print("delete user")
                    elif event.key == pg.K_3:
                        user_choice = 3
                    elif event.key == pg.K_4:
                        user_choice = 4
                    elif event.key == pg.K_5:
                        user_choice = 5

                    user_choice = all_users[user_choice]
                    if user_choice not in items_menu:
                        pass
            pg.display.flip()

    def display_level_menu(self):
        while True:
            self.menu = Menu(self, "Click Me ! -- Level Menu")
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

    def main_menu(self):
        main_menu = Menu(self, "Main Menu")
        current_user = self.user.get_current_user()
        if current_user:
            menu_items = [
                f"current user : {current_user}", "Choose game level"]
            self.current_user = current_user
        else:
            menu_items = ["Create user"]
        main_menu.init_items(menu_items)
        main_menu.draw_menu()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.key == pg.K_1 and not current_user:
                    self.user.create_user()
                if event.key == pg.K_1 and current_user:
                    self.display_user_menu()
                if event.key == pg.K_2 and current_user:
                    self.display_level_menu()

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

    def display_result(self):
        self.end_timestmap = time.time()
        time_score = round(self.end_timestmap - self.start_timestamp, 2)
        self.screen.fill((0, 0, 0))
        self.user.write_score(self.current_user, time_score)
        text_score = f"Your score is {time_score} seconds !"
        Helper.display_text(game, text_score, WIDTH/2, HEIGHT/2)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()

                    if event.key == pg.K_RETURN:
                        Game.count = 0
                        self.display_level_menu()
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.start_game()
