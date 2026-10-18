class Vocation():
    def __init__(self, dict):
        self.name = dict["name"]
        self.vigor_multiplier = dict["vigor_multiplier"]
        self.strength_multiplier = dict["strength_multiplier"]
        self.magic_multiplier = dict["magic_multiplier"]
        self.hp_multiplier = dict["hp_multiplier"]