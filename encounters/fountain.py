import random
from math import floor

from encounters.encounter import Encounter
from ui import ui


class Fountain(Encounter):

    def run(self):
        ui.set_header("Encounter - Fountain")
        # Set the scene and ask player to make a choice.
        ui.print("You stumbled into a grove with a fountain at the centre.", 2)
        choice = ui.prompt("Do you approach the fountain? (y/n) ").lower()

        if choice in ["y", "yes"]:
            # Randomly choose an outcome if the player approaches.
            roll = random.random()

            if roll < 0.2:
                # 20% chance to level up.
                ui.print("You carefully approach the fountain.", 0.5)
                ui.print("The spirit of the fountain emerges from the water and blesses you!", 2)
                self.player.level_up()

            elif roll > 0.9:
                # 10% chance to take 5% damage (1 damage minimum).
                damage = max(floor(self.player.max_hp * 0.05), 1)
                self.player.hp -= damage
                ui.print(f"A fairy emerges from behind the fountain and bites you! \nTook {damage} damage.", 2)

            else:
                # 70% chance to heal by 10%
                heal = floor(self.player.max_hp * .1)
                self.player.hp = min(
                    self.player.hp + heal, 
                    self.player.max_hp
                )
                ui.print("You find a nice place to rest for a little while.", 0.5)
                ui.print("Recovered 10% of your HP.", 2)
        
        else:
            # When the player chooses not to approach.
            ui.print("You avoid the fountain and continue on your way.", 2)