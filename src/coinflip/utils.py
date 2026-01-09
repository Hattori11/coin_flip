import random


def decide_first_choice(player_1, player_2):
    """Retorna um jogador aleatório entre dois"""
    return random.choice([player_1, player_2])

def opposite_side(choice):
    return "coroa" if choice == "cara" else "cara"