# Constant variables
ITEMS = {
    "coke": 150,
    "sprite": 150,
    "fanta": 150,
    "orange juice": 130,
    "water": 100
}
VALID_COINS = [5, 10, 20, 50, 100, 200]


def main():
    owed = select_item() 

    while owed > 0:
        print(f"Owed: {owed}")

        try:
            coin = int(input("Insert coin: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        
        if coin in VALID_COINS:
            owed -= coin
        else:
            print("Invalid coin")

    print(f"Change: {abs(owed)}")


def select_item():
    while True:
        selection = input("Select item: ").lower()

        if selection in ITEMS:
            return ITEMS[selection]

        print("Please select from:")
        for item in ITEMS:
            print(f"  - {item}")


# Main guard
if __name__ == "__main__":
    main()