from item import Item
from ui import ui

class VendingMachine():

    def __init__(self, items: list[Item], valid_coins):
        self.items = {item.name: item for item in items}
        self.valid_coins = valid_coins


    def run(self):
        # Prompt the user to select an item from a list of options.
        item = ui.choice(
            "Select item: ", 
            [item.name for item in self.items.values()], 
            self.validate_item
        )
        price = item.price
        change = self.process_payment(item.name, price)
        self.end_transaction(item.name, change)


    def process_payment(self, name, price):
        owed = price
        while owed > 0:
            # Update header with latest info.
            ui.set_header(f"Item: {name.capitalize()}    Outstanding: {owed}")

            # Prompt for a valid coin.
            coin = ui.prompt("Insert coin: ", self.validate_coin, "coin")

            # Subtract the coin from the amount owed.
            owed -= coin
            ui.print("Coin accepted.", 0.5)

        return owed


    def end_transaction(self, name, change):
        ui.set_header(f"Item: {name.capitalize()}    Outstanding: 0")
        ui.print(f"Change: {abs(change)}", 0.5)
        ui.print("Transaction complete!", 2)


    # Ensure user input a valid item.
    def validate_item(self, input):
        if input in self.items:
            return self.items[input]


    # Ensure user input is a valid coin.
    def validate_coin(self, input):
        try:
            coin = int(input)
            if coin in self.valid_coins:
                return coin
        except:
            # User didn't input a number.
            return None










# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


ITEMS = [ 
    Item(name = "coke",  price = 150),
    Item(name = "water", price = 100),
    Item(name = "pepsi", price = 150),
    Item(name = "juice", price = 130),
]

VALID_COINS = [5, 10, 20, 50, 100, 200]


def main():
    vm = VendingMachine(ITEMS, VALID_COINS)
    vm.run()


if __name__ == "__main__":
    main()