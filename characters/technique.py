class Technique():
    
    def __init__(self, dict):
        self.name = dict["name"]
        self.vocations = dict["vocations"]
        self.main_stat = dict["main_stat"]
        self.stat_multiplier = dict["stat_multiplier"]