class InvalidChoiceError(Exception):
    pass

class Player:
    def __init__(self, name):
        self.name = name
        self.consecutive_victories = 0

    def add_victory(self):
        self.consecutive_victories += 1

    def choice_side_coin(self):
        """Pergunta ao jogador qual sua escolha de lado da moeda"""
        while True:
            try:
                choice = input("Escolha o lado da moeda (cara ou coroa): ").lower()

                if choice not in ("cara", "coroa"):
                    raise InvalidChoiceError(
                        f"Escolha inválida: {choice}"
                    )

                return choice

            except InvalidChoiceError as e:
                print(e)