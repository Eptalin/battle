import random
from math import floor

from encounters.encounter import Encounter


class Fountain(Encounter):

    def run(self):
        # Set the scene and ask player to make a choice.
        print("You stumbled into a grove with a fountain at the centre.")
        choice = input("Do you approach the fountain? (y/n) ").lower()

        if choice in ["y", "yes"]:
            # Randomly hoose an outcome if the player approaches.
            roll = random.random()
            if roll < 0.2:
                # 20% chance to level up.
                print("The spirit of the fountain emerges from the water and blesses you!")
                self.player.level_up()

            elif roll > 0.9:
                # 10% chance to take 5% damage (1 damage minimum).
                damage = max(floor(self.player.max_hp * 0.05), 1)
                self.player.hp -= damage
                print(f"A fairy emerges from behind the fountain and bites you! \nTook {damage} damage.")

            else:
                # 70% chance to heal by 10%
                heal = floor(self.player.max_hp * .1)
                self.player.hp = min(
                    self.player.hp + heal, 
                    self.player.max_hp
                )
                print("You find a nice place to rest for a little while. \nRecovered 10% of your HP.")
        
        else:
            # When the player chooses not to approach.
            print("You avoid the fountain and continue on your way.")