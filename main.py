from game import Game


def main():
    
    # Create gamestate and run.
    try:
        game = Game()
        game.run()

    # Exit gracefully when user inputs Ctrl^C
    except KeyboardInterrupt:
        print("\nQuitting game.")
        return

    # Catch and report errors, while hiding traceback.
    # except Exception as e:
    #     print(f"An error occured:\n{e}")


if __name__ == "__main__":
    main()