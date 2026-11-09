from textwrap import dedent

from characters.player import Player
from characters.player_vocations import VOCATIONS
from characters.vocation import Vocation
from ui import ui


# Guide users to create a character.
class CharacterCreator():

    # Control the character creation flow.
    def create(self):
        ui.set_header("Character Creation")
        while True:
            # Prompt for name and vocation.
            name = ui.prompt("What's your hero's name? ").title()
            vocation = ui.choice(
                 "Please select your vocation: ", 
                 [vocation['name'].capitalize() for vocation in VOCATIONS.values()], 
                 self.validate_vocation
            )

            # Create a player instance using that info.
            player = Player(name, vocation)

            if self.is_confirmed(player):
                # If the player is happy with their choices, return the player instance.
                return player


    # Allow the user to select a vocation from a list.
    def validate_vocation(self, selection):
        if selection in VOCATIONS:
            return Vocation(VOCATIONS[selection])
        return None


    # Display current player settings and prompt user for confirmation.
    def is_confirmed(self, player):
        # Print character sheet and prompt user to confirm.
        confirmation = ui.prompt(dedent(f"""\
            Are you happy with these choices?
            
            Name:       {player.name}
            Vocation:   {player.vocation.name.capitalize()}
            - Strength: {player.strength}
            - Magic:    {player.magic}
            - Max HP:   {player.max_hp}

            (Y/n): """
        )).lower()

        if confirmation in ["y", "yes"]:
                return True
        return False