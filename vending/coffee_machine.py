import time

from ui import ui

class CoffeeMachine():

    def run(self):
        # Choose coffee type.
        coffee = ui.choice(
            "How would you like your coffee?",
            ["black", "white"]
        )

        # Choose milk if white.
        if coffee == "white":
            milk = ui.choice(
                "What kind of milk?",
                ["full cream", "low fat", "almond", "soy"]
            )
            coffee = f"{milk} coffee"

        # Choose whether to add sugar.
        sugar = ui.choice(
            "Would you like sugar?",
            ["yes", "no"]
        )

        # Choose sugar quantity if required.
        if sugar == "yes":
            quantity = ui.prompt(
                "How many teaspoons? ",
                validate=lambda x: int(x) if x.isdigit() and int(x) > 0 else None,
                noun="quantity"
            )
            coffee += f" with {quantity} teaspoons of sugar"

        # Prepare coffee.
        ui.clear()
        ui.print("Preparing your coffee...")
        for _ in range(3):
            ui.print(". ", 1)

        # Serve coffee.
        ui.print(f"\nHere's your {coffee}!")
