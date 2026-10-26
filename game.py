from textwrap import dedent

from characters.character_creator import CharacterCreator
from overworld.overworld import Overworld


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


    def game_over(self):
        print(dedent(f"""
            {self.player.name} has fallen...

            ========= Results =========
            Distance travelled: {self.overworld.distance_travelled}km
            Enemies defeated:   {self.player.enemies_defeated}
            ===========================

            Thank you for playing!
        """))