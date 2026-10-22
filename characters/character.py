from math import floor


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
        self.strength = floor(self.level * self.vocation['strength_multiplier'])
        self.magic    = floor(self.level * self.vocation['magic_multiplier'])
        self.max_hp   = floor(self.level * self.vocation['hp_multiplier'])
        self.techniques = self.get_techniques()


    # Increment level and recalculate stats.
    def level_up(self):
        self.level += 1
        self.update_charsheet()
        print(f"You have levelled up! Now Lvl.{self.level}")


    # TODO: Build list of techniques accessible to the character.
    def get_techniques(self):
        return None