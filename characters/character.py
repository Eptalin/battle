from characters.vocation import Vocation


class Character():

    def __init__(self, name, vocation, level):
        self.name     =  name
        self.vocation = Vocation(vocation)
        self.level    = level
        self.update_charsheet()
        self.hp       = self.max_hp


    def update_charsheet(self):
        self.strength = self.level * self.vocation.vigor_multiplier
        self.magic = self.level * self.vocation.strength_multiplier 
        self.max_hp = self.level * self.vocation.magic_multiplier
        self.techniques = self.get_techniques()


    def level_up(self):
        self.level += 1
        self.update_charsheet()
        print(f"You have levelled up! Now Lvl.{self.level}")


    def get_techniques(self):
        return None