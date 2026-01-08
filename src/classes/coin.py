import random as r


class Coin:
    def __init__(self):
        self.sides = ["Cara", "Coroa"]
    
    def throw_up(self):
        """Escolhe um dos lados da moeda aleatoriamente"""
        return r.choice(self.sides)