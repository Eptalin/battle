from encounters.encounter import Encounter


class FairyFountain(Encounter):

    def run(self):
        print("You stumbled into a grove with a fountain at the centre.")
        choice = input("Do you approach the fountain? (y/n)").lower()

        if choice in ["y", "yes"]:
            print("A fairy emerges from behind the fountain and blesses you!")
            self.player.level_up()

        else:
            print("You avoid the fountain and continue on your way.")