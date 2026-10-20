from characters.vocation import Vocation


class Character():

    def __init__(self, name, vocation, level):
        self.name     =  name
        self.vocation = Vocation(vocation)
        self.level    = level
        self.update_charsheet()
        self.hp       = self.max_hp


    def update_charsheet(self):
        self.vigor = self.calc_vigor()
        self.strength = self.calc_strength()
        self.magic = self.calc_magic()
        self.max_hp = self.calc_max_hp()
        self.techniques = self.get_techniques()


    def level_up(self):
        self.level += 1
        self.update_charsheet()
        self.hp = self.max_hp


    def calc_vigor(self):
        return 1 * self.level * self.vocation.vigor_multiplier


    def calc_strength(self):
        return 1 * self.level * self.vocation.strength_multiplier
        
        
    def calc_magic(self):
        return 1 * self.level * self.vocation.magic_multiplier


    def calc_max_hp(self):
        return 10 * self.level * self.vocation.hp_multiplier


    def get_techniques(self):
        return None