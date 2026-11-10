from math import floor

from characters.technique import Technique
from characters.technique_list import TECHNIQUES
from ui import ui


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
        # Record current info.
        old_strength = self.strength
        old_magic = self.magic
        old_max_hp = self.max_hp
        old_hp = self.hp
        hp_percentage = self.hp / self.max_hp

        # Apply level up.
        self.level += 1
        self.update_charsheet()
        self.hp = floor(self.max_hp * hp_percentage)

        # Print level up.
        ui.print(f"{self.name} has levelled up! Now Lvl.{self.level}", 1, "\n\n")
        ui.print(f"Name:       {self.name}", 0.2)
        ui.print(f"Vocation:   {self.vocation.name.capitalize()}", 0.2)
        ui.print(f"- Strength: {old_strength} → {self.strength}", 0.2)
        ui.print(f"- Magic:    {old_magic} → {self.magic}", 0.2)
        ui.print(f"- HP:       {old_hp}/{old_max_hp} → {self.hp}/{self.max_hp}", 5)



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