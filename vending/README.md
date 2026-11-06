# Vending

Rough flow for teaching Object-Oriented Programming and Polymorphism.

## Basic script:

`coke.py`

1. Essentially like our C implementation. Program just runs line by line from top to bottom.
2. Main guard.
   
`vending.py`

3. Global variables / *constants*.
4. Error handling with Try-Except.
5. Define helper function `slect_item()`.
   - input normalisation with `.lower()`.


## OOP Introduction: `vending_machine.py`

1. Define `class VendingMachine`.
2. Define `__init__` and class properties.
3. Define class methods, `select_item()` and `process_payment()`.
4. Show basic usage example.
   - Create object instance.
   - Define *constants*, `ITEMS` and `VALID_COINS` for simplicity.


## OOP Inheritance: `vanding_machine_mk2.py`

1. Define child class `class VendingMachineMk2(VendingMachine)`
   - Get all the `VendingMachine` properties and methods automatically.
2. Define new version of super() method `ProcessPayment()`.
   - If user chooses cash, use the super() version.
   - If user chooses card, we follow a new flow.
3. Define an additional method for the child, `no_internet()`.
   - Card payment unavailable, so can just use super() method for cash.


## Polymorphism: `polymorph.py`

1. Define `select_machine()` method to choose between vending machines.
2. Define `run_machine()` method, which works regardless of which version is input.
   - Add `run()` method to the parent class `VendingMachine`.
3. Create a new machine class, `CoffeeMachine`.
   - No properties this time, but need a `run()` method.
4. Update `select_machine()` to add `CoffeeMachine`.
   - Super different functionality from the same `run_machine()` function.


## User Interface: `ui.py`

1. 