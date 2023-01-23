import pygame as pg
from Helper import *
from CSVHandler import *
from Menu import *


class User:

    def __init__(self, game):
        self.game = game

    def create_user(self):
        new_user = Helper.display_input(self.game)
        # self.write_score(new_user, 0)
        return new_user

    def get_all_users(self):
        all_users = []
        all_users_data = CSVHandler.read_all_data()
        for user in all_users_data:
            if user not in all_users:
                all_users.append(user)
        return all_users

    def get_current_user(self):
        data = CSVHandler.read_all_data()
        try:
            current_user = data[-1]
            return current_user
        except IndexError:
            return False

    def write_score(self, user, score):
        data = {"user": user, "score": score}
        CSVHandler.write_csv_file(data)

    def change_current_user(self):
        while True:
            user_menu = Menu(self.game, "Change User Menu")
            items_menu = self.get_all_users()
            user_menu.init_items(items_menu)
            user_menu.draw_menu()
            for event in pg.event.get():
                Helper.check_quit_game(event)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        return items_menu[0]
                    elif event.key == pg.K_2:
                        return items_menu[1]
                    elif event.key == pg.K_3:
                        return items_menu[2]
                pg.display.flip()

    def choose_user_to_delete(self):
        while True:
            delete_user_menu = Menu(self.game, "Delete a user")
            items_menu = self.get_all_users()
            delete_user_menu.init_items(items_menu)
            delete_user_menu.draw_menu()

            user_to_delete = 0

            for event in pg.event.get():
                Helper.check_quit_game(event)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        return items_menu[0]
                    if event.key == pg.K_2:
                        return items_menu[1]
                    if event.key == pg.K_3:
                        return items_menu[2]
                pg.display.flip()


    def delete_user(self):
        user_to_delete = self.choose_user_to_delete()
        print(user_to_delete)
        CSVHandler.delete_all_row(user_to_delete)


    def get_10th_last_scores(self, user):
        last_scores = CSVHandler.get_all_data_by_row(row='user', value=user)
        # print(last_scores)
        return last_scores[-10:]