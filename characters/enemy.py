from character import Character

class Enemy(Character):

    def __init__(self, vocation, level):
        super().__init__(
            name     = vocation.name, 
            vocation = vocation, 
            level    = level
        )