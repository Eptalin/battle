from vending_machine import VendingMachine
from vending_machine_mk2 import VendingMachineMk2
from coffee_machine import CoffeeMachine
from item import Item
from ui import ui


ITEMS = [ 
    Item(name = "coke",  price = 150),
    Item(name = "water", price = 100),
    Item(name = "pepsi", price = 150),
    Item(name = "juice", price = 130),
]
VALID_COINS = [5, 10, 20, 50, 100, 200]


def main():
    ui.set_header("Machine Selection")
    
    machines = ["Vending Machine Mk1", "Vending Machine Mk2", "Coffee Machine"]
    machine = ui.choice("Select a machine: ", machines, validate_machine)
    
    if machine == "mk1":
         machine = VendingMachine(ITEMS, VALID_COINS)
         ui.set_header("Vending Mahchine Mk.1")
    
    if machine == "mk2":
         machine = VendingMachineMk2(ITEMS, VALID_COINS)
         ui.set_header("Vending Mahchine Mk.2")
    
    if machine == "coffee":
         machine = CoffeeMachine()
         ui.set_header("Coffee Machine")
    
    machine.run()


def validate_machine(machine):
        if machine in ["vending machine mk1", "vending machine 1", "vm1", "mk1", "1"]:
            return "mk1"
        elif machine in ["vending machine mk2", "vending machine 2", "vm2", "mk2", "2"]:
            return "mk2"
        elif machine in ["coffee machine", "coffee", "cm"]:
             return "coffee"
        return None       


if __name__ == "__main__":
    main()