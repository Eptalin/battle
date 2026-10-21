import random

from encounters.encounter import Encounter
from characters.enemy import Enemy
from characters.enemy_vocations import ENEMY_TYPES


class Battle(Encounter):

    def run(self):
        # Select an enemy type from the list and randomly set their level.
        enemy_type = random.choice(list(ENEMY_TYPES.values()))
        enemy_level = self.set_enemy_level(self.player.level)

        # Use those values to create an enemy instance.
        enemy = Enemy(enemy_type, enemy_level)

        # Print what we encountered.
        print(f"You have encountered a Lv.{enemy.level} {enemy.name}!")

        # TODO: Implement combat.
        print("The enemy hit you for 10 damage and fled.")
        self.player.hp -= 10


    # Randomly set the enemy's level using the player level as a base.
    def set_enemy_level(self, player_level):
        n = random.random()
        
        if n > .95:
            # 5% chance of super strong enemy
            return player_level + 2
        
        if n > .75:
            # 20% chance of strong enemy
            return player_level + 1
        
        if n < .05 and player_level > 2:
            # 5% chance of super weak enemy
            return player_level - 2
        
        if n < .25 and player_level > 1:
            # 20% chance of weak enemy
            return player_level - 1

        # 50% chance of normal strength enemy
        return player_level