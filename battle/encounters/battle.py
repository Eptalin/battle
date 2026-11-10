from math import floor

from characters.enemy_generator import generate_enemy
from characters.enemy_types import ENEMY_TYPES
from combat.combat import Combat
from encounters.encounter import Encounter
from ui import ui


class Battle(Encounter):

    def run(self):
        ui.set_header("Encounter - Battle")

        # Generate a random enemy from the full pool of all enemies.
        enemy = generate_enemy(list(ENEMY_TYPES.values()), self.player.level)

        # Print what we encountered.
        ui.print(f"You have encountered a Lv.{enemy.level} {enemy.name}!", 2)

        # Initiate combat.
        combat = Combat(self.player, enemy)
        combat.run()