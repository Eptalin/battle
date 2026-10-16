class Character():

    def __init__(self, name, vocation, level):
        self.name     = name
        self.vocation = vocation
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
