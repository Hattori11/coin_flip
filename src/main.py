from classes.coin import Coin
from classes.player import Player
from utils import decide_first_choice


def main():
    name = input("Informe o nome do jogador 1: ")
    player_one = Player(name)
    name = input("Informe o nome do jogador 2: ")
    player_two = Player(name)
    coin = Coin()

    while True:
        print("Se inicia o game!")
        first = decide_first_choice(player_one.name, player_two.name)
        if first == player_one.name:
            player_one.choice_side_coin()
        else:
            player_two.choice_side_coin()

        side = coin.throw_up()

        if side == player_one.choice:
            player_one.add_victory()
            player_two.clear_victories()
            if player_one.consecutive_victories == 3:
                print(f"O jogador {player_one.name} venceu!")
                break
            else:
                continue
        else:
            player_two.add_victory()
            player_one.clear_victories()
            if player_two.consecutive_victories == 3:
                print(f"O jogador {player_two.name} venceu!")
                break
            else:
                continue


if __name__ == "__main__":
    main()
