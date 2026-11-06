import os
import subprocess
from textwrap import dedent
from time import sleep


# Controls the terminal display.
class UI():

    # Constructor
    def __init__(self):
        self.header = None


    def prompt(self, prompt, validate=lambda x:x, noun="input"):
        user_input = None
        while user_input is None:
            self.clear()
            user_input = validate(input(prompt))
            if user_input is None:
                self.invalid_input(noun)
        return user_input


    # Prompt user to select from a list of options.
    def choice(self, prompt, options, validate=lambda x:x, noun="selection"):
        choice = None
        while choice is None:
            self.clear()

            # Display the prompt.
            self.show_message(prompt, 0.2)

            # Display the options.
            for option in options:
                print(f"- {option.capitalize()}")
                self.pause(0.2)

            # Make sure the input is in the list of valid options.
            choice = validate(input("Selection: ").lower())

            # Reprompt if the input was invalid.
            if choice is None:
                self.invalid_input(noun)
        return choice


    def invalid_input(self, noun):
        self.clear()
        print(f"Invalid {noun}.")
        self.pause(2)


    # Display a message in the terminal.
    def show_message(self, message, pause=0):
        print(message)
        self.pause(pause)


    # Clear the terminal and display the header.
    def clear(self):
        self.clear_full()
        if self.header is not None:
            print(self.header)

    
    # Fully clear the terminal.
    def clear_full(self):
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


    # Pause the terminal output by n seconds.
    def pause(self, seconds=1):
        sleep(seconds)


    # Store a header for reuse.
    def set_header(self, label):
        self.header = dedent(f"""
        =============================================================================================

                {label}

        =============================================================================================
        """)
        self.clear()


# Create a single UI object to be shared throughout the program.
ui = UI()