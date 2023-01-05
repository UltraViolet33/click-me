import pygame as pg
from Helper import *
import sys


class User:

    def __init__(self, game):
        self.game = game

    def create_user(self):
        new_user = Helper.display_input(self.game)
        return new_user