from textwrap import dedent

from characters.character_creator import CharacterCreator
from overworld.overworld import Overworld
from ui import ui


class Game():

    def __init__(self):
        self.player = None
        self.character_creator = CharacterCreator()
        self.overworld = Overworld()
        


    def run(self):
        # Build Player character
        self.player = self.character_creator.create()

        while self.player.hp > 0:
            # Travel until the player encounters something in the overworld.
            encounter_type = self.overworld.travel()

            # Run the encounter
            encounter = encounter_type(self.player)
            encounter.run()
            
        # Print the game over results.
        self.game_over()



    # Report game over results.
    def game_over(self):
        ui.set_header("GAME OVER")

        # Use game state information if it exists.
        distance = self.overworld.distance_travelled    if self.overworld else 0
        enemies_defeated = self.player.enemies_defeated if self.player    else 0
        name = f"{self.player.name}'s"                  if self.player    else "Your"

        # Print the results template.
        ui.print(dedent(f"""\
            {name} journey has ended...

            ========= Results =========
            Distance travelled: {distance}km
            Enemies defeated:   {enemies_defeated}
            ===========================

            Thank you for playing!
        """), 2)