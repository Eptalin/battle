import random
from math import floor
from textwrap import dedent

from characters.enemy import Enemy
from characters.player import Player
from ui import ui


class Combat():

    # Constructor
    def __init__(self, player: Player, enemy: Enemy):
        self.turn = 1
        self.player = player
        self.enemy = enemy
        self.defending = set()



    # Control the overall flow of combat.
    def run(self):
        # Decide turn order.
        turn_order = self.set_turn_order()
        self.update_header()
        
        while self.characters_live():
            # Continue taking turns until one character's hp reaches 0.
            for character in turn_order:
                self.take_turn(character)
                # Update header.
                self.update_header()

                if not self.characters_live():
                    # Stop taking turns once a character dies.
                    break
            self.turn += 1

        # Report the battle results once one character's hp reaches 0.
        winner = self.report_winner()

        if winner == self.player: 
            # The player levels up when they win.
            winner.level_up()
            winner.enemies_defeated += 1

        return winner
        


    # Determine the turn order through dice rolls.
    def set_turn_order(self):
        # Have each character roll for initiative.
        player_roll = random.randint(1, 20) + self.player.strength
        enemy_roll  = random.randint(1, 20) + self.enemy.strength
        turn_order = [self.player, self.enemy] if player_roll > enemy_roll else [self.enemy, self.player]

        # Report turn order.
        ui.print(f"{turn_order[0].name} will act first!", 1.5)

        # Return a list of characters in order of their rolls.
        return turn_order



    # Control the flow for a single character's turn.
    def take_turn(self, actor):
        # Select the opponent based on who the actor is.
        opponent = self.enemy if actor == self.player else self.player
        ui.print(f"It's {actor.name}'s turn.", 1.5)

        # Reset defend status
        self.defending.discard(actor)

        # Select the technique to use.
        if actor != self.player:
            # Non-player attacks are chosen at random.
            technique = random.choice(actor.techniques)

        # Present a list of options to the player.
        else: 
            technique = ui.choice(f"Which technique do you want to use?", 
                  [f"{t.name} ({t.main_stat})" for t in actor.techniques],
                  lambda x: self.validate_technique(x, actor),
                  "technique")

        match technique.type:

            case "attack":
                ui.print(f"{actor.name} attacks!", 1)
                # Use the technique's main stat.
                attack_stat = getattr(actor, technique.main_stat)
                defence_stat = getattr(opponent, technique.main_stat)

                # Each participant rolls to see if the attack hits.
                attack_roll = random.randint(1, 20) + attack_stat
                defence_roll = random.randint(1,20) + defence_stat

                if attack_roll < defence_roll:
                    # End the actor's turn if the attack fails.
                    ui.print(f"{actor.name} failed to connect.", 2)
                    return

                # Deal one D6 + main stat damage.
                damage = random.randint(1, 6) + attack_stat

                # Halve damage if opponent is defending.
                if opponent in self.defending:
                    damage //= 2
                    ui.print(f"{opponent.name} braces for the attack.", 1.5)
                
                opponent.hp -= damage
                ui.print(f"{actor.name} deals {damage} damage to {opponent.name}!", 2)
 
            case "defend":
                # Add character to the list of defending characters.
                self.defending.add(actor)

                # Recover 15% of max hp (min 1hp)
                heal = max(floor(actor.max_hp * .15), 1)
                actor.hp += heal
                ui.print(f"{actor.name} takes a defensive posture and rests for a moment.", .5)
                ui.print(f"{actor.name} recovers {heal}hp.", 1.5)



    # Print the results of the battle.
    def report_winner(self):
        winner = self.player if self.player.hp > 0 else self.enemy
        loser = self.player if self.player.hp <= 0 else self.enemy
        ui.print(f"{winner.name} has defeated {loser.name}!", 2)
        return winner



    # Update the header with the latest info.
    def update_header(self):
        p = self.player
        e = self.enemy
        p.hp = p.hp if p.hp > 0 else 0
        e.hp = e.hp if e.hp > 0 else 0
        ui.set_header(dedent(f"""\
            Combat: Turn {self.turn}

            {p.name} 
            Lvl.{p.level} {p.vocation.name.capitalize()}: {p.hp}/{p.max_hp} HP    VS    Lvl.{e.level} {e.name}: {e.hp}/{e.max_hp} HP\
        """))



    # Return True if both characters are still alive.
    def characters_live(self):
        if self.player.hp > 0 and self.enemy.hp > 0:
            return True
        return False



    # Choose from a list of techniques.
    def validate_technique(self, choice, actor):
        return next((t for t in actor.techniques if t.name == choice), None)
