import random as r
import time as t


class Coin:
    def __init__(self):
        self.sides = ["cara", "coroa"]

    def throw_up(self):
        """Escolhe um dos lados da moeda aleatoriamente"""
        t.sleep(3)
        choice = r.choice(self.sides)
        print(f"Caiu {choice}!")
        return choice
