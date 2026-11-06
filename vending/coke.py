def main():
    owed = 150
    valid_coins = [5, 10, 20, 50, 100, 200]

    while owed > 0:
        print(f"Owed: {owed}")
        coin = int(input("Insert coin: "))
        if coin in valid_coins:
            owed -= coin
        else:
            print("Invalid coin")

    print(f"Change: {abs(owed)}")

if __name__ == "__main__":
    main()