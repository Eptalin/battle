from game import Game
from ui import ui

def main():
    
    # Create gamestate and run.
    try:
        game = Game()
        game.run()

    # Exit gracefully when user inputs Ctrl^C
    except KeyboardInterrupt:
        if game.overworld and game.player:
            ui.game_over(game.overworld, game.player)
        else:
            ui.game_over()
        return

    # Catch and report errors, while hiding traceback.
    # except Exception as e:
    #     print(f"An error occured:\n{e}")


if __name__ == "__main__":
    main()