from characters.character import Character


class Player(Character):
    def __init__(self, name, vocation):
        super().__init__(name, vocation, level=1)