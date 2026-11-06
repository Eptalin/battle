import random

from ui import ui
from vending_machine import VendingMachine


class VendingMachineMk2(VendingMachine):

    def process_payment(self, name, price):
        ui.set_header(f"Item: {name}    Outstanding: {price}")
        # Prompt user to pay by Cash or Card.
        payment_method = ui.prompt("Pay by cash or card? ", lambda s: s if s in ["cash", "card"] else None, "payment method").lower()

        if payment_method == "cash":
            return super().process_payment(name, price)

        # Card payment
        if random.random() > 0.5:
            # High roll means successful connection.
            ui.prompt("Tap card. (Press Enter to continue)")
            return 0

        # Low roll means connection issues.
        return self.no_internet(name, price)


    def no_internet(self, name, price):
        ui.clear()
        ui.show_message("Can't connect to server. Please pay by cash.")
        super().process_payment(name, price)




























# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


ITEMS = {
    "coke": 150,
    "sprite": 150,
    "fanta": 150,
    "orange juice": 130,
    "water": 100
}
VALID_COINS = [5, 10, 20, 50, 100, 200]

def main():
    vm = VendingMachineMk2(ITEMS, VALID_COINS)
    price = vm.select_item()
    vm.process_payment(price)
    print("Transaction complete!")


if __name__ == "__main__":
    main()