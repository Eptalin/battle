import random

from encounters.encounter_types import ENCOUNTERS


# A class which controls travel through the overworld.
class Overworld():

    # Constructor
    def __init__(self):
        self.distance_travelled = 0

    # Repeatedly increase distance travelled until interruped by an encounter.
    def travel(self):
        starting_distance = self.distance_travelled
        encounter_chance = .20  # Percentage chance of an encounter per iteration.
        distance_unit = 2       # How far we travel each iteration.
        encounter = None        # No encounter found yet.

        while encounter == None:
            # Increment the distance the player has travelled.
            self.distance_travelled += distance_unit

            if random.random() < encounter_chance:
                # Select an encounter from a list of possible encounters.
                encounter = random.choice(list(ENCOUNTERS.values()))

        # Print how far we travelled this round.
        self.print_travel(starting_distance)

        # Inform the game which encounter interrupted our travel.
        return encounter


    # Print the travel distance to the terminal.
    def print_travel(self, start):
        # TODO: Print it more like an animation.
        print(f"Travelled {self.distance_travelled - start} km")

