from random import random, choice

from characters.enemy import Enemy
from characters.player import Player
from characters.vocation import Vocation
from characters.enemy_vocations import ENEMY_TYPES


class Encounter():

    def __init__(self, player: Player):
        random_enemy = choice(list(ENEMY_TYPES))
        enemy_vocation = Vocation(ENEMY_TYPES[random_enemy])
        enemy_level = self.set_enemy_level(player.level)
        self.enemy = Enemy(enemy_vocation, enemy_level)


    def set_enemy_level(self, player_level):
        n = random()
        
        if n > .95:
            return player_level + 2
        
        if n > .75:
            return player_level + 1
        
        if n < .05 and player_level > 2:
            return player_level - 2
        
        if n < .25 and player_level > 1:
            return player_level - 1
        
        return player_level