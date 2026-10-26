from math import floor

from characters.technique import Technique
from characters.technique_list import TECHNIQUES


# The basic shape for all characters. Players, enemies, etc.
class Character():

    # Constructor
    def __init__(self, name, vocation, level):
        self.name     = name
        self.vocation = vocation
        self.level    = level
        self.update_charsheet()
        self.hp       = self.max_hp


    # Calculate stats (Round down to nearest integer)
    def update_charsheet(self):
        self.strength = floor(self.level * self.vocation.strength_multiplier)
        self.magic    = floor(self.level * self.vocation.magic_multiplier)
        self.max_hp   = floor(self.level * self.vocation.hp_multiplier)
        self.techniques = self.get_techniques()


    # Increment level and recalculate stats.
    def level_up(self):
        hp_percentage = self.hp / self.max_hp * 100
        self.level += 1
        self.update_charsheet()
        self.hp = self.max_hp * hp_percentage
        print(f"You have levelled up! Now Lvl.{self.level}")


    # Build list of techniques accessible to the character.
    def get_techniques(self):
        # Turn the dictionaries into Technique objects.
        techniques = [Technique(technique) for technique in TECHNIQUES]

        # Return techniques usable by the character's vocation.
        return [
            technique for technique in techniques
            if self.vocation.name in technique.vocations
            or "all" in technique.vocations
        ]