import pygame as pg
from Helper import *
from CSVHandler import *


class User:

    def __init__(self, game):
        self.game = game

    def create_user(self):
        new_user = Helper.display_input(self.game)
        self.write_score(new_user, 0)
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