import random


class Overworld():

    @staticmethod
    def travel():
        encounter_chance = .20
        distance_unit = 2
        travelled_distance = 0
        while True:
            if random.random() < encounter_chance and travelled_distance > 1:
                break
            travelled_distance += distance_unit
        Overworld.print_travel()
        return travelled_distance

    @staticmethod
    def print_travel():
        graphic = r'''
                                  O 
                                 /|\/
        .  .  .  .  .  .  .  .  ./ \
        ──────┬─────────┬─────────┬─────────┬────
              7         8         9         10     
        '''
        print(graphic)


    @staticmethod
    def generateEncounter():
        pass