from characters.character import Character


class Enemy(Character):

    def __init__(self, vocation, level):
        super().__init__(
            name = vocation.name.capitalize(), 
            vocation = vocation, 
            level = level,
        )