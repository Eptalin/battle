import os
import subprocess
from textwrap import dedent
from time import sleep

# Controls how information is displayed to the terminal.
class UI():

    # Constructor
    def __init__(self):
            self.header = None


    # Report game over results.
    def game_over(self, overworld=None, player=None):
        # Use game state information if it exists.
        distance = overworld.distance_travelled    if overworld else 0
        enemies_defeated = player.enemies_defeated if player    else 0
        name = f"{player.name}'s"                  if player    else "Your"

        # Print the results template.
        print(dedent(f"""
            {name} journey has ended...

            ========= Results =========
            Distance travelled: {distance}km
            Enemies defeated:   {enemies_defeated}
            ===========================

            Thank you for playing!
        """))


    # Erase the terminal.
    def clear(self):
        subprocess.run("cls" if os.name == "nt" else "clear")


    # Pause for n seconds.
    def pause(self, seconds=1):
        sleep(seconds)


# Create a UI object classes can import.
ui = UI()