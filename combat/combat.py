import random
from math import floor

from characters.enemy import Enemy
from characters.player import Player


class Combat():

    # Constructor
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.defending = set()


    # Control the overall flow of combat.
    def run(self):
        # Decide turn order.
        turn_order = self.set_turn_order()
        
        while self.characters_live():
            # Continue taking turns until one character's hp reaches 0.
            for character in turn_order:
                self.take_turn(character)

                if not self.characters_live():
                    # Stop taking turns once a character dies.
                    break

        # Report the battle results once one character's hp reaches 0.
        winner = self.report_winner()

        if winner == self.player: 
            # The player levels up when they win.
            winner.level_up()

        return winner
        

    # Determine the turn order through dice rolls.
    def set_turn_order(self):
        # Have each character roll for initiative.
        player_roll = random.randint(1, 20) + self.player.strength
        enemy_roll  = random.randint(1, 20) + self.enemy.strength

        # Return a list of characters in order of their rolls.
        return [self.player, self.enemy] if player_roll > enemy_roll else [self.enemy, self.player]


    # Control the flow for a single character's turn.
    def take_turn(self, actor):
        # Select the opponent based on who the actor is.
        opponent = self.enemy if actor == self.player else self.player
        print(f"It's {actor.name}'s turn.")

        # Reset defend status
        self.defending.discard(actor)

        # Select the technique to use.
        technique = self.choose_technique(actor)

        match technique.type:

            case "attack":
                # Use the technique's main stat.
                attack_stat = getattr(actor, technique.main_stat)
                defence_stat = getattr(opponent, technique.main_stat)

                # Each participant rolls to see if the attack hits.
                attack_roll = random.randint(1, 20) + attack_stat
                defence_roll = random.randint(1,20) + defence_stat

                if attack_roll < defence_roll:
                    # End the actor's turn if the attack fails.
                    print(f"{actor.name}'s attack failed to connect.")
                    return

                # Deal one D6 + main stat damage.
                damage = random.randint(1, 6) + attack_stat

                # Halve damage if opponent is defending.
                if opponent in self.defending:
                    damage //= 2
                    print(f"{opponent.name} braces for the attack.")
                
                opponent.hp -= damage
                print(f"{actor.name} deals {damage} damage to {opponent.name}!")
 
            case "defend":
                # Add character to the list of defending characters.
                self.defending.add(actor)

                # Recover 15% of max hp (min 1hp)
                heal = max(floor(actor.max_hp * .15), 1)
                actor.hp += heal
                print(f"{actor.name} takes a defensive posture and rests for a moment. \n{actor.name} recovers {heal}hp.")


    # Print the results of the battle.
    def report_winner(self):
        winner = self.player if self.player.hp > 0 else self.enemy
        loser = self.player if self.player.hp <= 0 else self.enemy
        print(f"{winner.name} has defeated {loser.name}!")
        return winner


    # Return True if both characters are still alive.
    def characters_live(self):
        if self.player.hp > 0 and self.enemy.hp > 0:
            return True
        return False


    # Choose from a list of techniques.
    def choose_technique(self, actor):
        if actor != self.player:
            # Non-player attacks are chosen at random.
            return random.choice(actor.techniques)

        # Present a list of options to the player.
        print(f"Which technique do you want to use?")
        for technique in actor.techniques:
            print(f" - {technique.name.capitalize()} ({technique.main_stat.capitalize()})")

        while True:
            # Continue prompting until user selects a valid technique.
            choice = input("Choice: ").lower()
            
            technique = next((t for t in actor.techniques if t.name == choice), None)
            if technique is not None:
                return technique
            
            print("Technique not found in list.")
