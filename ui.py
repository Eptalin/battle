import os
import subprocess
from textwrap import indent
from time import sleep

# Controls how information is displayed to the terminal.
class UI():

    # Constructor
    def __init__(self):
            self.header = None



    # Prompt the user for input (optionally, validate it).
    def prompt(self, prompt, validate=lambda x:x, noun="input"):
        user_input = None
        while user_input is None:
            self.clear()

            # Display the prompt.
            user_input = validate(input(prompt))
            
            # Reprompt if the input was invalid.
            if user_input is None:
                self.clear()
                self.print(f"Invalid {noun}", 1.5)
        return user_input



    # Prompt user to select from a list of options (optionally, validate it).
    def choice(self, prompt, options, validate=lambda x:x, noun="selection"):
        choice = None
        while choice is None:
            self.clear()

            # Display the prompt.
            self.print(prompt, 0.2, "\n\n")

            # Display the options.
            for option in options:
                print(f"- {option.title()}")
                self.pause(0.2)

            # Make sure the input is in the list of valid options.
            choice = validate(input("\nSelection: ").lower())

            # Reprompt if the input was invalid.
            if choice is None:
                self.clear()
                self.print(f"Invalid {noun}", 1.5)
        return choice



    # Display a message in the terminal.
    def print(self, message, pause=0, end="\n"):
        print(message, end=end, flush=True)
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
        bar = "=" * 90
        label = indent(label, " " * 8)
        self.header = f"\n{bar}\n\n{label}\n\n{bar}\n"
        self.clear()



# Create a single UI object to be shared throughout the program.
ui = UI()