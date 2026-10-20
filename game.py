from characters.character_creator import CharacterCreator
from encounter.encounter import Encounter
from overworld.overworld import Overworld


class Game():

    def __init__(self):
        self.player = None
        self.distance_travelled = 0
        self.game_over = False
        

    def run(self):
        
        # build Player character
        self.player = CharacterCreator.create()

        # print(f"Name: {self.player.name}")
        # print(f"Vocation: {self.player.vocation.name.capitalize()}")
        # print(f"  - Vigor:    {self.player.vigor}")
        # print(f"  - Strength: {self.player.strength}")
        # print(f"  - Magic:    {self.player.magic}")
        # print(f"  - Max HP:   {self.player.max_hp}")


        while True:
        # loop:
            # walk a bit -> random chance of encounter per unit of distance
            self.distance_travelled += Overworld.travel()
                # talent flag: decrease encounter chance, shorter distance (Mage: Invisibility)
                # taleng flag: increase encounter chance, longer distance (Fighter: Some kind of charge)

            engagement = Generate_Engagement(self.player)

            # if encounter: 
                # randomly select enemy (set level randomly within range around player)
                    # talent flag: chance to decrease enemy level (Ranger: Some kind of debilitation)

                # battle
                    # if lose:
                        # game over
                        # break
                
                    # if win:
                        # level up player
                        # continue
            break
        print(self.distance_travelled)