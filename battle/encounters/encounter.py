from characters.player import Player


# The most basic shape of an encounter
class Encounter():

    def __init__(self, player: Player):
        self.player = player

    # All Encounter child classes must implement their own run() method
    def run(self):
        raise NotImplementedError

