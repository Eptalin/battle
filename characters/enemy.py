import random

from character import Character


class Enemy(Character):

    def __init__(self, vocation, player_level):
        super().__init__(
            name     = vocation.name, 
            vocation = vocation, 
            level    = self.set_level(player_level))


    def set_level(self, player_level):
        n = random.random()
        if n < .25 and player_level > 1:
            return player_level - 1
        if n > .75:
            return player_level + 1
        if n > .95:
            return player_level + 2
        return player_level