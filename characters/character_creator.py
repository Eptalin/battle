from characters.player_vocations import VOCATIONS
from characters.player import Player


class CharacterCreator():

    @staticmethod
    def create():
        name = input("What's your hero's name? ")
        vocation = None

        print("Please select your vocation:")
        for vocation in VOCATIONS.values():
            print(f" - {vocation['name'].capitalize()}")
        selection = input("Selection: ").lower()

        if selection in VOCATIONS:
            vocation = VOCATIONS[selection]

        return Player(name, vocation)