from characters.player import Player
from characters.player_vocations import VOCATIONS
from characters.vocation import Vocation


# Guide users to create a character.
class CharacterCreator():

    # Control the character creation flow.
    def create(self):
        while True:
            # Prompt for name and vocation.
            name = input("What's your hero's name? ")
            vocation = self.choose_vocation() 

            # Create a player instance using that info.
            player = Player(name, vocation)

            if self.is_confirmed(player):
                # If the player is happy with their choices, return the player instance.
                return player


    # Allow the user to select a vocation from a list.
    def choose_vocation(self):
        while True:
            # Prompt for a vocation, and display a list of options.
            print("Please select your vocation:")
            for vocation in VOCATIONS.values():
                print(f" - {vocation['name'].capitalize()}")
            selection = input("Selection: ").lower()

            # Validate user input
            if selection in VOCATIONS:
                return Vocation(VOCATIONS[selection])


    # Display current player settings and prompt user for confirmation.
    def is_confirmed(self, player):
        # Print character sheet.
        print(f"Name:     {player.name}")
        print(f"Vocation: {player.vocation.name.capitalize()}")
        print(f"  - Strength: {player.strength}")
        print(f"  - Magic:    {player.magic}")
        print(f"  - Max HP:   {player.max_hp}")

        # Ask if the user is happy with their choices.
        confirmation = input("\nAre you happy with this selection? (Y/n) ").lower()

        if confirmation in ["y", "yes"]:
                return True
        return False