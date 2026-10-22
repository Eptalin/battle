from math import floor

from characters.enemy_generator import generate_enemy
from characters.enemy_types import ENEMY_TYPES
from encounters.encounter import Encounter


class Battle(Encounter):

    def run(self):
        # Generate a random enemy from the full pool of all enemies.
        enemy = generate_enemy(list(ENEMY_TYPES.values()), self.player.level)

        # Print what we encountered.
        print(f"You have encountered a Lv.{enemy.level} {enemy.name}!")

        # TODO: Implement combat.
        damage = max(floor(self.player.max_hp * .1), 1) # 10% damage (at least 1 damage)
        self.player.hp -= damage
        print(f"The enemy hit you for {damage} damage and fled.")
